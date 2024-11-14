from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the driver (Chrome, Firefox, etc.)
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

print("Opening WhatsApp Web...")
driver.get("https://web.whatsapp.com")

# Automatically wait 15 seconds for user to scan QR code
print("Waiting for you to scan the QR code...")
time.sleep(15)

# Initialize an empty list to store phone numbers
phone_numbers = []

try:
    # Wait for the elements to load
    print("Waiting for WhatsApp to load...")
    time.sleep(5)
    
    # Loop through a large range, adjust according to the number of items visible in WhatsApp Web
    for i in range(1, 4001):  # For 4000 numbers
        try:
            print(f"Attempting to locate phone number {i}...")
            
            # Use indexed XPath to get each phone number
            phone_xpath = f"(//div[@aria-label='Chat list']//div[@role='gridcell']//span[@title]') and @data-pre-plain-text][contains(text(), '+')])[{i}]"
            # phone_number_element = driver.find_element(By.XPATH, phone_xpath)

            phone_number = phone_number_element.text
            print(f"Found phone number {i}: {phone_number}")
            
            # Append to list
            phone_numbers.append(phone_number)
            
        except Exception as e:
            print(f"Could not locate number {i} or another issue occurred: {e}")
            break  # Exit loop if there are no more numbers visible

finally:
    print("Closing the driver...")
    driver.quit()

# Check if any phone numbers were collected
if phone_numbers:
    print("Saving data to Excel...")
    # Save the phone numbers to an Excel file
    try:
        df = pd.DataFrame(phone_numbers, columns=["Phone Numbers"])
        df.to_excel("whatsapp_phone_numbers.xlsx", index=False)
        print("Data successfully saved to whatsapp_phone_numbers.xlsx")
    except Exception as e:
        print(f"Failed to save data to Excel: {e}")
else:
    print("No phone numbers were collected.")

driver.find_elements (By.XPATH, "//div[@aria-label='Chat list']//div[@role='gridcell']//span[@dir='auto']")