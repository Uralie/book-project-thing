import sys
import os
import cv2
import scan

print("starting")
image = cv2.imread("image.png")
print(image.shape)
print("scanning")
scanned = scan.scan(image)
print("scanned")

cv2.imshow("Image", scanned)

cv2.waitKey(0)
cv2.destroyAllWindows()