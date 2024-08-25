# Example from GeeksforGeeks https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/
# We import the necessary packages
#import the needed packages
import cv2
import os
# import argparse
import pytesseract
from PIL import Image
from sys import platform

if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# dir = "./img"

#camera_index is the video device number of the camera 
camera_index = 0
cap = cv2.VideoCapture(camera_index)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)
ret,frame = cap.read()
cv2.imwrite('img/c1.png',frame)

cap.release()

#convert to grayscale image
gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# #checking whether thresh or blur
# if args["pre_processor"]=="thresh":
#     cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
# if args["pre_processor"]=="blur":
#     cv2.medianBlur(gray, 3)
        
#memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
f = open("pg1.txt", "w")
f.write(text)
f.close
    
# show the output images
'''
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)
'''