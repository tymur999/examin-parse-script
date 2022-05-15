from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
from os import listdir
#print(pytesseract.image_to_string(Image.open('test.png')))
filepath = "C:\\Users\\dongd\\Downloads\\Testin\\CoreSet\\"


"""
Rudimentary script to convert pdf to jpeg images for use in OCR.
"""
def pdf2image(filepath):
    num = 0
    for pages in range(0,140,10):
        images = convert_from_path("apworld3.pdf",400,first_page=pages, last_page=pages+10)
        for i, image in enumerate(images):
            num+=1
            fname = str(num)+'.jpg'
            image.save(filepath + fname, "JPEG")