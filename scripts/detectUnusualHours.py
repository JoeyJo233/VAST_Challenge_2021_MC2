import csv
import os
import util as d
import pandas as pd

with open('NameStartFinish.csv', 'r') as data:
    reader = csv.reader(data)
    # Skip the header row
    next(reader)
    with open('SusPeople.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        first_row = ["FirstName","LastName","Start","Finish","TimeStart","TimeFinish"]
        writer.writerows([first_row])
        for row in reader:
            if pd.to_datetime(row[4]).hour > 20 or pd.to_datetime(row[4]).hour < 6:
                writer.writerow(row)
