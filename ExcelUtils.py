import pandas as pd

class ExcelUtils:
    def __init__(self):
        self.data = None

    def read_contacts(self, file_path):
        """Reads contacts from the Excel file and returns a list of dictionaries."""
        df = pd.read_excel(file_path)
        contacts = df.to_dict('records')  # Converts each row to a dictionary
        return contacts
