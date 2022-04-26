import pyautogui 
from PIL import Image
import pytesseract
from datetime import datetime
import time

# https://github.com/tesseract-ocr/tesseract#installing-tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
t1=datetime.now()
while True:
    img = pyautogui.screenshot() 
    width, height = img.size
    img = img.crop((width/2, height/2, width, height-10))
    result = pytesseract.image_to_string(img)
    if 'Fishing Bobber splashes' in result:

        t = datetime.now()
        print('Fish caught!', t, 'Time took to catch a fish', t-t1)
        #print('yes')
        pyautogui.click(button='right')
        time.sleep(1)  #we have to wait for subtitle to disappear
        pyautogui.click(button='right')
        time.sleep(4)  #also the minimum time to catch a fish is 5 seconds
        t1 = datetime.now()