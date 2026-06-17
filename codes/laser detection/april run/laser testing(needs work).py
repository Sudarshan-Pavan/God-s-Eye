import cv2

image = cv2.imread('laser photos for study/Screenshot 2024-04-30 123838.png0')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imwrite('C:\projects\hsv_blue.jpg', hsv_image)

cv2.imshow('HSV image', hsv_image)
cv2.waitKey('m')
cv2.destroyAllWindows()