import cv2
from mathFunctions import simplify
import pytesseract

def getText(filename):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
    try:
        return [text.replace("\n",""),eval(text.strip().replace(" ","").replace("\n",""))]
    except Exception:
        return text.strip().replace("\n","")

import cv2
vidPath="./vid4.mp4"
cap=cv2.VideoCapture(vidPath)
ret=True
while ret:
    if ret:
        ret,frame=cap.read() # return bool, frame
        cv2.imshow('frame',frame)
        cv2.imwrite('tempImg.jpg',frame)
        print(getText("tempImg.jpg"))
        if cv2.waitKey(25) & 0xFF==ord('k'):
            break