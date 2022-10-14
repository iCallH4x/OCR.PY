import cv2
import numpy as np
import pytesseract
import pyperclip
import pyautogui
import os, sys

from PIL import ImageGrab, ImageOps
import time
import re
from pynput import keyboard

from config import TESSERACT_DIR

res = 0
ocr = True

# Get Platform by sys.platform, linux = linux, darwin = mac (for some reason I cba to research)
if sys.platform == "linux" or sys.platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = 'tesseract'
else:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_DIR

while ocr:
    # ask user if they would like to loop the ocr
    ocr = input("Would you like to constantly update the clipboard? Type 'y' if you are trying to snipe keys (y/n)").lower()
    break

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def on_press(key):
    if key == keyboard.Key.esc:
        return False
def wait_for_esc():
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()

def coords():

    print('-----------------------------------')
    print('              OCR.py               ')
    print('-----------------------------------\n')
    print('To get started you have to point your mouse in the first corner\nwhere you would like the tool to scan and confirm with the ESC-Key')
    wait_for_esc()
    x1,y1 = pyautogui.position()
    print('Corner 1 set. Now move to the 2nd corner and confirm with ESC')
    wait_for_esc()
    x2,y2 = pyautogui.position()
    print('Corner 2 set.')
    clearConsole()
    print('----------------------------------------------------')
    print('Got Following Positions:')
    print('Corner 1 x: %s y: %s , Corner 2: x: %s y: %s'%(str(x1),str(y1),str(x2),str(y2)))
    print('----------------------------------------------------\n')
    return x1,y1,x2,y2

x1,y1,x2,y2 = coords()

cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
cap_arr = np.array(cap)
text = pytesseract.image_to_string(cap)
text = text.strip()
if len(text) > 20:
    print(text)
    pyperclip.copy(text)

if ocr == "y":
    while True:
        cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        cap_arr = np.array(cap)
        text = pytesseract.image_to_string(cap)
        text = text.strip()
        if len(text) > 20:
            print(text)
            pyperclip.copy(text)
        time.sleep(0.1)

cv2.destroyAllWindows()


