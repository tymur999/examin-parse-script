import re
import pygsheets
import pandas as pd
#Authorization
gc = pygsheets.authorize(service_file="C:\\Users\\dongd\\Downloads\\Testin\\testin-350221-d130e9dfc50a.json")


"""
Script to parse through the questions from the text file and upload them to the google sheets
File paths and data is hard coded for simplicity as this is not intended to run outside the IDE

"""


df = pd.DataFrame()
sh = gc.open("Question Database")
wks = sh[1]  #Sheet to Target

doUpload = True #Toggle upload to sheets

with open('C:\\Users\\dongd\\Downloads\\Testin\\test.txt', 'r') as f:
    QNum = 1
    offset = 110 #Initial starting row #
    copy = False
    questionString = ""
    A= ""
    AC = False
    B= ""
    BC = False
    C= ""
    CC = False
    D= ""
    DC = False
    lines = f.readlines()
    for line in lines:
        if (str(QNum) + ".") in line.strip():
            print(D + "\n")
            copy = True
            DC = False
            if doUpload:
                wks.update_value( (QNum+offset,5), D)
            D = ""
        if "(A)" in line.strip():
            copy = False
            AC = True
            QNum += 1
            print(questionString)
            if doUpload:
                wks.update_value( (QNum+offset,1), questionString)
            questionString = ""
        if "(B)" in line.strip():
            BC = True
            AC = False
            print(A + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,2), A)
            A = ""
        if "(C)" in line.strip():
            CC = True
            BC = False
            print(B + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,3), B)
            B = ""
        if "(D)" in line.strip():
            DC = True
            CC = False
            print(C + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,4), C)
            C = ""
        if copy:
            questionString+=line.strip() + " "
        if AC:
            A += line.strip() + " "
        if BC:
            B += line.strip() + " "
        if CC:
            C += line.strip() + " "
        if DC:
            D += line.strip() + " "
    
        

