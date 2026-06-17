import cv2

image_path = "C:\stse\sem5\POCV\imgs\LP (1).jpg"

try:
    # Attempt to open the image file
    image = cv2.imread(image_path)
    
    if image is not None:
        # Image was successfully loaded
        # Process the image or perform any desired operations
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # Image failed to load
        print(f"Failed to open image: {image_path}")

except Exception as e:
    # Exception occurred while opening the image
    print(f"Error opening image: {e}")
