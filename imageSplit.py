from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
from os import listdir
import imageio

#pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\dongd\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
#print(pytesseract.image_to_string(Image.open('image32.jpg')))
folder_dir = "C:\\Users\\dongd\\Downloads\\Testin\\QuestionsSet\\"


def question_split():
    print(folder_dir)
    for images in os.listdir(folder_dir):
        if images.endswith('.jpg'):
            img = imageio.imread(folder_dir + images)
            height, width, _ = img.shape

            # Cut the image in half
            width_cutoff = width // 2
            s1 = img[:, :width_cutoff, :]
            s2 = img[:, width_cutoff:, :]
            print(width_cutoff)
            # Save each half
            imageio.imwrite("C:\\Users\\dongd\\Downloads\\Testin\\SplitSet\\" + images[:-4] + '-0.jpg', s1)
            imageio.imwrite("C:\\Users\\dongd\\Downloads\\Testin\\SplitSet\\" + images[:-4] + '-1.jpg', s2)
question_split()