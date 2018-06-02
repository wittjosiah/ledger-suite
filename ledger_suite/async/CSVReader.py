import csv
from .DataFetcher import DataFetcher

class CSVReader(DataFetcher):
    def fetch(self, path, headers = []):
        csvData = []

        with open(path, newline='') as csvfile:
            csvReader = csv.reader(csvfile)
            for row in csvReader:
                dataEntry = {}
                for idx, value in enumerate(row):
                    if len(headers) - 1 >= idx:
                        dataEntry[headers[idx]] = value
                    else:
                        dataEntry[idx] = value
                csvData += [dataEntry]

        return csvData
