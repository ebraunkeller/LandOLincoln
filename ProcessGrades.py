#Process Grades. Invoke python ProcessGrades.py
# Takes the large file and creates <school><grade> files and selects fields
#STUDENT_NUMBER
#GRADE_LEVEL
#SCHOOLID
#NAME
#SUBJECTAREA
#STORECODE
#SCORE
cols=['STUDENT_NUMBER','GRADE_LEVEL','SCHOOLID','NAME','SUBJECTAREA','STORECODE','SCORE']

import pandas as pd
import csv


Ifile='C:\Users\Elaine\Documents\BKL\CC93\RawData\StandardsAchievementT116-17.csv'
Ofile='C:\Users\Elaine\Documents\BKL\CC93\RawData\Grades.csv'

df=pd.read_csv(Ifile,dtype='str')
df1=df[cols]
df1.rename(columns={'STUDENT_NUMBER':'StudentID'}, inplace=True)

df1.to_csv(Ofile,index=False)   