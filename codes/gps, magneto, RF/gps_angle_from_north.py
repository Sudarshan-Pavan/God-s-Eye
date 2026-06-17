import math

def calculate_bearing(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the differences in longitudes
    delta_lon = lon2 - lon1

    # Calculate the bearing angle
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.atan2(y, x)

    # Convert bearing from radians to degrees
    bearing_deg = math.degrees(bearing)
    return (bearing_deg + 360) % 360

# Coordinates of Groud Station
# AB1 co-ordinates
ground_lat = 16.4951
ground_lon = 80.5012

# Coordinates of Drone
# main entrance co-ordinates
drone_lat = 16.4975
drone_lon = 80.4993  

bearing = calculate_bearing(ground_lat, ground_lon, drone_lat, drone_lon)
print(f"Bearing from Your Location to Destination: {bearing:.2f} degrees clockwise from North.")
