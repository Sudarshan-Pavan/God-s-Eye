#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi
#raspberry pi

from gpiozero import LED
import time

# Define the GPIO pin number connected to the transmitter module
transmitter_pin = 17
transmitter = LED(transmitter_pin)

def transmit_value(value):
    binary_value = bin(value)[2:]  # Convert the value to binary
    print("Transmitting:", binary_value)
    
    for bit in binary_value:
        if bit == '1':
            transmitter.on()
        else:
            transmitter.off()
        
        time.sleep(0.5)  # Adjust the delay based on your RF module's characteristics

# Example usage
try:
    while True:
        user_input = int(input("Enter a value to transmit (0-255): "))
        if 0 <= user_input <= 255:
            transmit_value(user_input)
        else:
            print("Value must be between 0 and 255")
except KeyboardInterrupt:
    print("\nTransmission stopped")
finally:
    transmitter.off()  # Turn off the transmitter when the program ends
