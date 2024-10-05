import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  # Radius of Earth in kilometers. Use 3956 for miles.
    distance_km = r * c
    distance_meters = distance_km * 1000  # Convert to meters
    return distance_meters


def calculate_route_id(df, threshold=1):
    df['TimeDiff'] = df['Timestamp'].diff().dt.total_seconds().div(60).fillna(0)
    df['RouteID'] = (df['TimeDiff'] > threshold).cumsum()
    df = df.drop(columns=['TimeDiff'])
    return df