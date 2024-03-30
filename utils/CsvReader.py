import csv
import os

from params import *

file = os.path.dirname(__file__) + "/../data/data.csv"


def read_csv_to_fill_data():
    # Open the CSV file
    with open(file, newline='') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        # Iterate over each row in the CSV file
        for row in csvreader:
            x.append(float(row[2]))
            y.append(float(row[3]))
            z.append(float(row[1]))
