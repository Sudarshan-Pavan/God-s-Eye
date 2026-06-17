#include <math.h>

// Function to calculate bearing
double calculate_bearing(double lat1, double lon1, double lat2, double lon2) {
    // Convert degrees to radians
    lat1 = radians(lat1);
    lon1 = radians(lon1);
    lat2 = radians(lat2);
    lon2 = radians(lon2);

    // Calculate the differences in longitudes
    double delta_lon = lon2 - lon1;

    // Calculate the bearing angle
    double y = sin(delta_lon) * cos(lat2);
    double x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(delta_lon);
    double bearing = atan2(y, x);

    // Convert bearing from radians to degrees
    double bearing_deg = degrees(bearing);
    return fmod((bearing_deg + 360), 360); // Ensure the value is between 0 and 360
}

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    
    // Coordinates of Ground Station
    // AB1 co-ordinates
    double ground_lat = 16.4951;
    double ground_lon = 80.5012;
    
    // Coordinates of Drone
    // main entrance co-ordinates
    double drone_lat = 16.4975;    
    double drone_lon = 80.4993;  

    // Calculate the bearing
    double bearing = calculate_bearing(ground_lat, ground_lon, drone_lat, drone_lon);
}

void loop() {
    // Empty loop
}
