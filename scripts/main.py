import csv
import pandas as pd
import util as d
import os

originalGpsData = pd.read_csv('data/csv/gps.csv')
assignmentData = pd.read_csv('data/csv/car-assignments.csv')
allPOI = pd.read_csv('data/csv/poi.csv')
newGpsData = pd.read_csv('data/csv/gpsWithNameandRoute.csv', low_memory=False)

#Which id to extract route data for
id = 23
all_ids = newGpsData['id'].unique()

if not os.path.exists('NameStartFinish.csv'):
    with open('NameStartFinish.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        data = ["Name","Start","Finish","TimeStart","TimeFinish","rout_id"]
        writer.writerow(data)
        for id in all_ids:
            dataWithID = newGpsData[newGpsData['id'] == id]
            route_ids = sorted(dataWithID['RouteID'].unique())
            for route_id in route_ids:
                route_data = dataWithID[(dataWithID['RouteID'] == route_id)]
                startlat35 = float(route_data.iloc[0]['lat'])
                startlong35 = float(route_data.iloc[0]['long'])
                stoplat35 = float(route_data.iloc[-1]['lat'])
                stoplong35 = float(route_data.iloc[-1]['long'])
                for index, row in allPOI.iterrows():
                    distance = d.haversine(row['lat'], row['long'], startlat35, startlong35)
                    allPOI.loc[index, 'Distance'] = distance

                closest_row = allPOI.loc[allPOI['Distance'].idxmin()]
                #print(f'{route_data.iloc[0]["FirstName"]} started trip at {pd.to_datetime(route_data.iloc[0]['Timestamp'])} closest to: ', closest_row['name'])
                s_closet_row = closest_row.copy()

                for index, row in allPOI.iterrows():
                    distance = d.haversine(row['lat'], row['long'], stoplat35, stoplong35)
                    allPOI.loc[index, 'Distance'] = distance
                closest_row = allPOI.loc[allPOI['Distance'].idxmin()]

                # print(pd.to_datetime(route_data.iloc[0]['Timestamp']).date())
                data = [[route_data.iloc[0]["FirstName"], route_data.iloc[0]["LastName"], s_closet_row['name'],closest_row['name'],
                pd.to_datetime(route_data.iloc[0]['Timestamp']), pd.to_datetime(route_data.iloc[-1]['Timestamp']),route_id]]
                
                writer.writerows(data)
                #print(f'{route_data.iloc[0]["FirstName"]} ended trip at {pd.to_datetime(route_data.iloc[-1]['Timestamp'])} closest to: ', closest_row['name'])

else:
    print(f"File already exists.") 



