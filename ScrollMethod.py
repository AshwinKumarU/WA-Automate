from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("Waiting for WhatsApp Web to load...")
time.sleep(20)  # Fixed 15-second wait for WhatsApp Web to load after QR code scan

# Log and timeout settings
scroll_pause_time = 2  # Time to pause between scrolls
timeout = 30  # Maximum time to wait before stopping
start_time = time.time()  # Record start time for timeout
contact_names = set()  # Store unique contact names

# Find the chat list container
try:
    print("Locating chat list container...")
    chat_list = driver.find_element(By.XPATH, '//div[@aria-label="Chat list"]')
except Exception as e:
    print("Failed to locate the chat list container:", e)
    driver.quit()
    exit()

# Scroll and collect contact names
previous_contact_count = 0
print("Starting contact extraction...")

try:
    while True:
        # Check if timeout has been exceeded
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print("Timeout exceeded. Closing the browser.")
            driver.quit()
            exit()

        # Find all visible contact names in the chat list
        visible_contacts = chat_list.find_elements(By.CSS_SELECTOR, 'span[title]')
        
        # Add new contacts to the set
        for contact in visible_contacts:
            contact_name = contact.get_attribute("title")
            if contact_name:
                contact_names.add(contact_name)
        
        # Log progress
        print(f"Collected {len(contact_names)} contacts so far...")
        
        # Check if new contacts were added
        if len(contact_names) == previous_contact_count:
            print("No new contacts detected. Reached the end of the contact list.")
            break  # End scrolling if no new contacts are loaded
        else:
            # Update previous contact count and reset timeout
            previous_contact_count = len(contact_names)
            start_time = time.time()  # Reset the timeout clock with progress

        # Scroll down the chat list
        print("Scrolling down to load more contacts...")
        ActionChains(driver).move_to_element(chat_list).click().send_keys(Keys.PAGE_DOWN).perform()
        
        # Pause to allow new contacts to load
        time.sleep(scroll_pause_time)

except Exception as e:
    print("An error occurred during scrolling:", e)

# Save contacts to Excel
df = pd.DataFrame(list(contact_names), columns=["Contact Name"])
df.to_excel("WhatsApp_Contacts.xlsx", index=False)
print("Contacts saved to WhatsApp_Contacts.xlsx")

# Close the browser
driver.quit()
