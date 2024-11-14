import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load phone numbers from Excel
data = pd.read_excel('contacts.xlsx')


# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Ensure 'chromedriver' is installed and in PATH

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Please scan the QR code to log in.")
time.sleep(20)  # Wait for manual login

# Send messages in a loop
for index, row in data.iterrows():
    try:
        phone = row['Phone']
        bookable_link = row['Bookable_Link']
        payment_link = row['Payment_Link']

        # Construct a dynamic message
        message = (
            f"Hello! Please select your slot to get a callback: {bookable_link}. "
            f"You can also make a payment using: {payment_link}. "
            f"Thank you!"
        )

        print(f"Sending message to {phone}...")

        # Open chat with the phone number
        url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
        driver.get(url)
        time.sleep(10)  # Wait for the chat to load

        # Send the message by pressing Enter
        input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
        input_box.send_keys(Keys.ENTER)

        print(f"Message sent to {phone}.")
        time.sleep(5)  # Delay to avoid being rate-limited

    except Exception as e:
        print(f"Failed to send message to {phone}: {str(e)}")

# Close the browser after sending all messages
driver.quit()