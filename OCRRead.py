import pytesseract
from PIL import Image
import os
from os import listdir
import imageio
import time
import glob
questions_dir = "C:\\Users\\dongd\\Downloads\\Testin\\SplitSet\\"
answers_dir = "C:\\Users\\dongd\\Downloads\\Testin\\AnswersSet\\"
Output_dir = "C:\\Users\\dongd\\Downloads\\Testin\\"

pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\dongd\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


def OCR_Questions():
    with open('C:\\Users\\dongd\\Downloads\\Testin\\test.txt', 'w') as f:
        for images in os.listdir(questions_dir):
            if images.endswith('.jpg'):
                #f.write(pytesseract.image_to_string(Image.open(folder_dir + images)))
                pyt = pytesseract.image_to_string(Image.open(questions_dir + images), lang='eng',config='--psm 6')
                f.write(pyt)
                print(pyt)
                f.write("\n")
                
    print("Job finished")

def OCR_Answers():
    with open('C:\\Users\\dongd\\Downloads\\Testin\\AnswersData.txt', 'w') as f:
        for i in range(84,144):
            try:
                img = Image.open(answers_dir + str(i) + '.jpg')
                img = img.crop((200, 370, 1550, 700))   #--> Skill Crop
                imageio.imwrite(Output_dir + "answerTemp"+ '.jpg', img)
                pyt = pytesseract.image_to_string(Image.open(Output_dir + "answerTemp"+ '.jpg'), lang='eng',config='--psm 6')
                f.write(pyt)
                print(pyt)
                f.write("\n")
                img = Image.open(answers_dir + str(i) + '.jpg')
                img = img.crop((1580, 370, 2450, 700)) # ---> Learning Objective Crop
                imageio.imwrite(Output_dir + "answerTemp"+ '.jpg', img)
                time.sleep(1)
                pyt = pytesseract.image_to_string(Image.open(Output_dir + "answerTemp"+ '.jpg'), lang='eng',config='--psm 6')
                f.write(pyt)
                print(pyt)
                f.write("\n")
                img = Image.open(answers_dir + str(i) + '.jpg')
                img = img.crop((2480, 470, 2650, 640)) # --> Unit Crop
                imageio.imwrite(Output_dir + "answerTemp"+ '.jpg', img)
                pyt = pytesseract.image_to_string(Image.open(Output_dir + "answerTemp"+ '.jpg'), lang='eng',config='--psm 10')
                f.write("Unit" + pyt)
                print(pyt)
                f.write("\n")
                img = Image.open(answers_dir + str(i) + '.jpg')
                img = img.crop((200, 685, 2700, 3700)) # --> Question Crop
                imageio.imwrite(Output_dir + "answerTemp"+ '.jpg', img)
                pyt = pytesseract.image_to_string(Image.open(Output_dir + "answerTemp"+ '.jpg'), lang='eng',config='--psm 6')
                f.write(pyt)
                print(pyt)
                f.write("\n")
            except:
                print("Missing File " + str(i))
                continue

    print("Job finished")

OCR_Answers()