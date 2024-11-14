import pandas as pd

class ExcelLibrary:
    def __init__(self):
        self.data = None

    def load_excel(self, file_path):
        """Loads the Excel file and stores data for further use."""
        self.data = pd.read_excel(file_path)

    def get_urls(self):
        """Returns a list of URLs from the Excel file if loaded."""
        if self.data is not None:
            return self.data['URL'].tolist()
        else:
            raise ValueError("Excel file not loaded. Call 'load_excel' with the file path first.")
