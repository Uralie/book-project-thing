# Example from GeeksforGeeks https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/
# We import the necessary packages
#import the needed packages
import cv2
import os
# import argparse
import pytesseract
from PIL import Image
from sys import platform
import ollama

if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
 
dir = "./img"

for fn in os.listdir(dir):
    #We then read the image with text
    images=cv2.imread(dir + "/" + fn)
    name = fn.split(".")[0]
    
    #convert to grayscale image
    gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    
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
    f = open(name + ".txt", "w")
    f.write(text)
    f.close
    print("Starting summary")
    response = ollama.chat(model='phi3', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
    print(response['message']['content'])
    f = open(name + "_summary.txt", "w")
    f.write(response['message']['content'])
    f.close


    # show the output images
    '''
    cv2.imshow("Image Input", images)
    cv2.imshow("Output In Grayscale", gray)
    cv2.waitKey(0)
    '''