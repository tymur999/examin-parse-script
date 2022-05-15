import re
import pygsheets
import pandas as pd
#Authorization
gc = pygsheets.authorize(service_file="C:\\Users\\dongd\\Downloads\\Testin\\testin-350221-d130e9dfc50a.json")



df = pd.DataFrame()
sh = gc.open("Question Database")
wks = sh[1]

doUpload = True

with open('C:\\Users\\dongd\\Downloads\\Testin\\AnswersData.txt', 'r') as f:
    QNum = 1
    offset = 0
    copy = False
    SkillString = ""
    LearningObjective = ""
    LCopy = False
    Unit = ""
    UnitCopy = False

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
        if ("Skill") in line.strip():
            print(D + "\n")
            copy = True
            DC = False
            if doUpload:
                wks.update_value( (QNum+offset,10), D)
            D = ""
        if ("Learning Objective") in line.strip():
            copy = False
            LCopy = True
            print(SkillString + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,17), SkillString)
            SkillString = ""
        if ("Unit") in line.strip():
            LCopy = False
            UnitCopy = True
            print(LearningObjective + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,18), LearningObjective)
            LearningObjective = ""
        if "(A)" in line.strip():
            UnitCopy = False
            AC = True
            QNum +=1
            print(Unit + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,19), Unit)
            if "Correct" in line.strip():
                wks.update_value( (QNum+offset,12), "A")
            Unit = ""
        if "(B)" in line.strip():
            BC = True
            AC = False
            print(A + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,7), A)
            if "Correct" in line.strip():
                wks.update_value( (QNum+offset,12), "B")
            A = ""
        if "(C)" in line.strip():
            CC = True
            BC = False
            print(B + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,8), B)
            if "Correct" in line.strip():
                wks.update_value( (QNum+offset,12), "C")
            B = ""
        if "(D)" in line.strip():
            DC = True
            CC = False
            print(C + "\n")
            if doUpload:
                wks.update_value( (QNum+offset,9), C)
            if "Correct" in line.strip():
                wks.update_value( (QNum+offset,12), "D")
            C = ""
        if copy:
            SkillString +=line.strip() + " "
        if AC:
            A += line.strip() + " "
        if BC:
            B += line.strip() + " "
        if CC:
            C += line.strip() + " "
        if DC:
            D += line.strip() + " "
        if LCopy:
            LearningObjective += line.strip() + " "
        if UnitCopy:
            Unit += line.strip() + " "

        
    
        

