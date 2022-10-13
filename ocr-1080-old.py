import cv2
import numpy as np
import pytesseract
import pyperclip

from PIL import ImageGrab

# U need Python
# And Some libaries
# pip install opencv-python
# pip install numpy
# pip install Pillow
# pip install pyperclip

# pip install pytesseract
# also read https://pypi.org/project/pytesseract/


while True:

    #Perfect in Twitches Cinema-Mode
    cap = ImageGrab.grab(bbox=(1020, 900, 1550, 992))
    cap_arr = np.array(cap)


    cv2.imshow("", cap)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    text = pytesseract.image_to_string(cap)


    text = text.strip()


    if len(text) > 20:
        print(text)
        pyperclip.copy(text)


    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
