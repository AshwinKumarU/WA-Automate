import pywhatkit
import openpyxl
import datetime

# Load the Excel file and extract data
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []  # Store tuples of (mobile_number, message)
    
    # Read rows from the second row onwards (ignoring headers)c

    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        mobile_number, message = row
        data.append((str(mobile_number), message))
    
    return data

def send_whatsapp_messages(data):
    for mobile_number, message in data:
        try:
            # Send WhatsApp message instantly
            pywhatkit.sendwhatmsg_instantly(mobile_number, message, wait_time=10)
            print(f"Message sent to {mobile_number}")
        except Exception as e:
            print(f"Failed to send message to {mobile_number}: {e}")

if __name__ == "__main__":
    excel_data = read_excel("contacts.xlsx")  # Adjust path if necessary
    send_whatsapp_messages(excel_data)
