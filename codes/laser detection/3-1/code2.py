import cv2
import time

img1 = cv2.imread('C:\stse\sem5\POCV\imgs\laser5.jpg')
img2 = cv2.imread('C:\stse\sem5\POCV\imgs\laser4.jpg')


img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
img_org = img1
img1 = img1[:,:,2]
img2 = img2[:,:,2]

diff = cv2.absdiff(img1, img2)
diff = cv2.medianBlur(diff,5)
ret, diff = cv2.threshold(diff ,0 ,255 ,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite("output1.png", diff)

count = 0

height, width = diff.shape[:2]

start = time.time() # time start

for y in range(height):
    for x in range(width):
        if diff[y,x] == 255:
            count += 1
        elif not count == 0:
            img_org[y, round(x - count/2)] = [0, 255, 0]
            count = 0

end = time.time() # time stop
print(end - start)

cv2.imwrite("output2.png", img_org)

cv2.waitKey(0)