#include <math.h>

// Function to calculate haversine distance
double haversine_distance(double lat1, double lon1, double lat2, double lon2) {
    // Earth's radius in kilometers
    double R = 6371.0;

    // Convert degrees to radians
    lat1 = radians(lat1);
    lon1 = radians(lon1);
    lat2 = radians(lat2);
    lon2 = radians(lon2);

    // Differences in coordinates
    double dlat = lat2 - lat1;
    double dlon = lon2 - lon1;

    // Haversine formula components
    double a = sin(dlat / 2) * sin(dlat / 2) + cos(lat1) * cos(lat2) * sin(dlon / 2) * sin(dlon / 2);
    double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    // Calculate distance
    double distance = R * c;
    return distance;
}

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    
    // Coordinates for Ground Station
    double lat1 = 16.4964;
    double lon1 = 80.5007;
    
    // Coordinates for Drone
    double lat2 = 34.0522;    
    double lon2 = -118.2437;  

    // Calculate the distance
    double distance = haversine_distance(lat1, lon1, lat2, lon2);
    
    // Print the distance to the Serial Monitor
    Serial.print("Distance between Ground Station and the Drone: ");
    Serial.print(distance, 4);  // Print with 2 decimal places
    Serial.println(" kilometers");
}

void loop() {
    // Empty loop
}
