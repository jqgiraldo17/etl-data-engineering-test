import csv

class DataExtraction:
    def __init__(self):
        pass
    
    def validate_data(self, row, csv_column):
       
        if csv_column not in row or row[csv_column] is None or row[csv_column] == "":
            return False

        try:
            primary_key = int(row[csv_column])
            if primary_key <= 0:
                return False
        except ValueError:
            return False

        return True

    def extract_data_from_csv(self, file_path, csv_column):
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if self.validate_data(row, csv_column):
                    data.append(row)
        return data                                                                            