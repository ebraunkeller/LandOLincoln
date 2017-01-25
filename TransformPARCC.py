# TransformPARCC
# extract just the fields we need for PARCC analysis:
# sudentID, test, score, PerformanceLEvel
# rename the fields PARCC_
# rename the tests to Reading and Mathematics for joining with MAP
# and write out PARCC.csv
import csv, pandas as pd

Test_Names={'E':'Reading', 'M':'Mathematics'}
Fields=['StudentID','Discipline','Score','Performance Level']
NewFieldNames={'Score':'PARCC_Score','Performance Level':'PARCC_PrfLvl'}

#Files
#input file
file="C:\Users\Elaine\Documents\BKL\CC93\RawData\ISBE_PARCC_Score 15-16 for BKL.csv"
dfP=pd.read_csv(file, dtype='str')
dfP1=dfP[Fields]
dfP1.rename(columns=NewFieldNames, inplace=True)
dfP1.Discipline=dfP1.Discipline.replace(Test_Names)
dfP1.to_csv('C:\Users\Elaine\Documents\BKL\CC93\RawData\PARCC.csv',index=False)
