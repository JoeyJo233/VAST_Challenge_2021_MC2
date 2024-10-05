import pandas as pd 
import util as d
gpsData = pd.read_csv('data/csv/gps.csv')
assignmentData = pd.read_csv('data/csv/car-assignments.csv')

# # Ensure the Timestamp column is treated as strings
# gpsData['Timestamp'] = gpsData['Timestamp'].astype(str)

# # Split the Timestamp into separate Date and Time columns
# gpsData['Date'] = gpsData['Timestamp'].str.split(' ').str[0]
# gpsData['Time'] = gpsData['Timestamp'].str.split(' ').str[1]

# # Ensure the Time column is treated as strings
# gpsData['Time'] = gpsData['Time'].astype(str)

# # Parse Time into separate Hours, Minutes, and Seconds columns by splitting the string
# gpsData['Hour'] = gpsData['Time'].str.split(':').str[0].astype(int)
# gpsData['Minute'] = gpsData['Time'].str.split(':').str[1].astype(int)
# gpsData['Second'] = gpsData['Time'].str.split(':').str[2].astype(int)


# # Get the FirstName of id 35 from assignmentData
# gpsData = gpsData.merge(assignmentData, left_on='id', right_on='CarID', how='left')

# gpsData.drop(columns=['Time','CarID'], inplace=True)

# # Save gpsData to a new CSV file
# gpsData.to_csv('data/csv/gpsWithNameandTime.csv', index=False)

mergedGpsData = pd.read_csv('data/csv/gpsWithNameandTime.csv', parse_dates=['Timestamp'])

unique_ids = sorted(mergedGpsData['id'].unique().tolist())
processed_dataframes = []

for id in unique_ids:
    id_data = mergedGpsData[mergedGpsData['id'] == id]

    mergedGpsData = mergedGpsData[mergedGpsData['id'] != id]
    id_data = d.calculate_route_id(id_data, 3)
    
    processed_dataframes.append(id_data)

mergedGpsData = pd.concat(processed_dataframes, ignore_index=True)

mergedGpsData.to_csv('data/csv/gpsWithNameandRoute.csv', index=False)

