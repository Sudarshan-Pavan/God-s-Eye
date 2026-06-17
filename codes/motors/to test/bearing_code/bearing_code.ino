#include <SoftwareSerial.h>

// SoftwareSerial for communication with GPS module
SoftwareSerial gpsSerial(7, 8);

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

// Function to get GPS coordinates
void get_gps_coordinates(double& ground_lat, double& ground_lon) {
    // Assume NMEA sentences are output from the GPS module
    // Replace these values with actual NMEA sentences from your GPS module
    String ground_lat_str = "ground_lat_value";
    String ground_lon_str = "ground_lon_value";

    // Convert string values to doubles
    ground_lat = lat_str.toDouble();
    ground_lon = lon_str.toDouble();
}

// Function to get GPS coordinates for the drone
void get_drone_gps_coordinates(double& drone_lat, double& drone_lon) {
    // Assume NMEA sentences are output from the RF transmitter connected to the drone's GPS module
    // Replace these values with actual NMEA sentences from your RF transmitter
    String drone_lat_str = "drone_lat_value";
    String drone_lon_str = "drone_lon_value";

    // Convert string values to doubles
    drone_lat = lat_str.toDouble();
    drone_lon = lon_str.toDouble();
}

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    gpsSerial.begin(9600);

    double ground_lat, ground_lon;
    get_gps_coordinates(ground_lat, ground_lon);

    double drone_lat, drone_lon;
    get_drone_gps_coordinates(drone_lat, drone_lon);

    // Calculate the bearing
    double bearing = calculate_bearing(ground_lat, ground_lon, drone_lat, drone_lon);
}

void loop() {
    // Empty loop
}