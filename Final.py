from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import quote

# Load phone numbers from Excel and drop NaN values
data = pd.read_excel('contacts.xlsx')
data = data.dropna(subset=['Phone'])

# Convert phone numbers from scientific notation to strings
numbers = data['Phone'].apply(lambda x: str(int(x))).tolist()

# Add + to each number
numbers = ['+' + number for number in numbers]

# Validate phone numbers: Check if each number is at least 10 digits
valid_numbers = [number for number in numbers if len(number) >= 11 and number[1:].isdigit()]

# Define your message with multiple lines and special characters
message = """Hi, thank you very much for your interest in Amura.

We are sending you this FAQ so that your immediate questions are addressed. After reading this, you can arrange for a consultation with one of our doctors.

Who is Amura?
Think of Amura as a hospital on the cloud, built to help you get healthy from lifestyle and chronic conditions. 

How to I connect with your doctors?
Now: Through WhatsApp. From 2025: Though Amura app.

How many times in a year can I talk to your doctors?
You can talk to our doctors and health coaches every day. They are available whenever you have a need.

What is special about Amura?
Amura uses diet and nutrition in an unique way to heal your body and get you to optimal health.

Is this allopathy?
Yes. All our programs are headed by qualified and registered medical doctors.

Is this scientific/evidence based?
Yes. Allopathy doctors cannot prescribe anything that is not evidence based.

Are there any side effects?
We are only going to ask you to make some lifestyle changes and be on regular vitamins and minerals. Nothing out of the ordinary.

What health conditions do you deal with?
Metabolic Health: Excess weight, PCOS, diabetes, hypertension, OSA, some GERD
Gut Health: Many (except, IBS/IBD, Crohn's, UC) 
Mental Health: Most cases of depression and anxiety
Autoimmune: On a case to case basis

Is it true that I can lose weight without exercise?
Yes. You need exercise for fitness, not for weight loss.

Then how will I lose weight?
You have seen someone who eats everything but never puts on weight, right? If you are putting on weight easily, then something inside your body is out of balance. When we find it and fix it, your weight will come off easily.

How to find out why I put on weight?
Book a consultation with our doctors (link at the bottom). They should be able to tell you why you put on weight and what to do about it.

How much should I pay?
- For Rs 4,000 you will get two very detailed consultations. 
- Each consultation will take 30 to 45 minutes. 
- After the first consultation, if required the doctor may ask you for some tests.
- During the second consultation, they will share their readings with you.

What happens after the consultation?
If the doctor's findings are favorable, then you can start the regular program to get to your good health. 

What should I do in your regular program?
Follow our every-day instructions. They are simple and easy. We are always there if you hit a hick up

How long will the regular program take?
Minimum 3 months. But be mentally prepared to spend at least 6 months. Some people may need more than a year even.

How much will the regular program cost me?
- We charge Rs 12,000/month. You will have to pay it once every three months, at the beginning (i.e. 36k).
- If you start the regular program within a month from your consultaiton, the Rs 4,000 you paid for the consultation will be adjusted from the above
- Other than that, you will need to keep some budget for the blood test. It may cost you 5k and you will need once every two months
- Lastly, we will ask you to take some vitamins, etc. That will cost you 5k to 8k per month

Are you using any fat burners or fat loss medicine?
No, none. 

Then why do I need vitamins?
Since you are going to be eating restricted food for a few months, you can become nutritionally deficient. If this happens to you, after stopping the diet you may start binging in order to top up the missing nutrients. The vitamins we give you are to avoid the nutrition famine.

Is there anything else I should know?
We bring the science to the table. Without your implementation this cannot succeed. Come onboard and make us proud.

OK...what is next?
Currently, we are flooded with a tremendous amount of enquiries, we sincerely apologise for the delay in reaching out, and we will need sometime to sort through everything. We are doing our best to get back to everyone and help them as best as we can. Thank you for your understanding.

Kindly ignore if you already received a response from us."""

# Encode the message for URL compatibility
encoded_message = quote(message)

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Ensure 'chromedriver' is installed and in PATH

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Please scan the QR code to log in.")
time.sleep(20)  # Wait for manual login

# Prepare a list to log the status of each message
log = []

# Send messages in a loop
for number in valid_numbers:
    status = "Failed"
    try:
        # Open chat with the phone number
        url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}"
        driver.get(url)

        try:
            # Wait for either the input box or the error element to load
            input_box = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'))
            )

            # Send the message if the input box is found
            input_box.click()
            input_box.send_keys(Keys.ENTER)
            status = "Passed"
            print(f"Message sent to {number}")
        except:
            # If input box is not found within 15 seconds, assume the number is invalid
            print(f"Failed to send message to {number}: Number not found or an error occurred.")

        time.sleep(5)  # Delay between messages to avoid being blocked

    except Exception as e:
        print(f"Failed to send message to {number}: {str(e)}")

    # Append result to the log
    log.append({"Phone": number, "Status": status, "Message": message})

# Close the browser after sending all messages
driver.quit()

# Create a DataFrame from the log
log_df = pd.DataFrame(log)

# Save the log to an output CSV, Excel, and JSON file
log_df.to_csv('message_log.csv', index=False)
log_df.to_excel('message_log.xlsx', index=False)
log_df.to_json('message_log.json', orient='records')

print("Message log has been saved to message_log.csv, message_log.xlsx, and message_log.json.")
