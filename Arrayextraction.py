from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (Chrome, Firefox, etc.)
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

print("Opening WhatsApp Web...")
driver.get("https://web.whatsapp.com")

# Automatically wait 15 seconds for user to scan QR code
print("Waiting for you to scan the QR code...")
time.sleep(15)
driver.implicitly_wait(10)

# Initialize an empty list to store phone numbers
phone_numbers = []

# Set up WebDriver
# driver = webdriver.Chrome()
# driver.get("YOUR_TARGET_URL")

# Locate elements and store text in a list
# try:
chat_elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@aria-label='Chat list']//div[@role='gridcell']//span[@dir='auto']"))
    )
# chat_elements = driver.find_elements(By.XPATH, "//div[@aria-label='Chat list']//div[@role='gridcell']//span[@dir='auto']")
chat_list_data = [element.text for element in chat_elements]
print(chat_list_data)
# Print out the chat list data
# for chat in chat_list_data:
#     print(chat)

# Close the driver
driver.quit()
