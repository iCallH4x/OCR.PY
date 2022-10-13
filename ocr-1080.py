import cv2
import numpy as np
import pytesseract
import pyperclip

from PIL import ImageGrab, ImageOps
import time
import re

# You need Python
# and some libraries
# pip install opencv-python
# pip install numpy
# pip install Pillow
# pip install pyperclip

# pip install pytesseract
# also read https://pypi.org/project/pytesseract/
res = 0

while True:

    #Perfect in Twitches Cinema-Mode
    cap = ImageGrab.grab(bbox=(1026, 912, 1535, 951)
    gray = ImageOps.grayscale(cap)
    cap_arr = np.array(gray)


    cv2.imshow("", cap_arr)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    text = pytesseract.image_to_string(cap_arr)


    text = text.strip()


    if len(text) > 20:
        if re.match("^.*(([\w\d]{5}-?){4}).*$",text):
            if res == 0:
                print("1 Got Text " + text)
                cache = text
                time.sleep(0.25)
                res = 1
            elif res == 1 and cache == text:
                res = 2
                print("2 Confirmed " + text)
                pyperclip.copy(text)

                time.sleep(10)
            elif res == 1 and cache != text:
                print("3 Unsure Retry " + cache + ' ' + text)
                res = 0
                time.sleep(0.25)
            else:
                res = 0

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
