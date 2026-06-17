import math

DLa = int
DLo = int

def haversine_distance(lat1, lon1, lat2, lon2):
    # Earth's radius in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula components
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    distance = R * c
    return distance

# Coordinates for Ground Station 
lat1 = 16.4964
lon1 = 80.5007

# Coordinates for Point B (Los Angeles)
lat2 = DLa
lon2 = DLo

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f"Distance between Ground Station and Drone: {distance:.2f} kilometers")
