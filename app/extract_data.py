import csv

class DataExtraction:
    """
    A class for validanting data and extracting it from CSV files.
    """

    def __init__(self):
        pass
    
    def validate_data(self, row, primary_key_column):
        """
        Validate if primary key values exist in the CSV data before loading into the table in MySQL.

        Args:
            row (str): The data from the database row containing the primary key value.
            primary_key_column (str): The name of the primary key column to validate.

        Returns:
            boolean: True if the primary keys exists in the .csv
        """
       
        if primary_key_column not in row or row[primary_key_column] is None or row[primary_key_column] == "":
            return False

        try:
            primary_key = int(row[primary_key_column])
            if primary_key <= 0:
                return False
        except ValueError:
            return False

        return True

    def extract_data_from_csv(self, file_path, csv_column):
        """
        Extracts the data from a given CSV

        Args:
            file_path (str): The path to the CSV file to be processed.
            csv_column (str): The name to the CSV column to extract data from.

        Returns:
            data (list): A list with the data processed.
        """
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if self.validate_data(row, csv_column):
                    data.append(row)
        return data                                                                            