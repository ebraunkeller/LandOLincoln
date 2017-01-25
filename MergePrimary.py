# Join student data with MAP assessment data
#File: MergeAll.py
#Purpose: Join student data and assessment data (NWEA, PARCC).Create the district and all the school/grade level files by df.loc method
#Input: Students.csv (generated) MAP.csv (generated) PARCC.csv (generated)
# New Input (try)  OLSAT.csv join by StudentNumber
#Output: District93.csv

import pandas as pd
import csv,gc

Sfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\Students.csv"
Mfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\MAP.csv"
Pfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\PARCC.csv"
OLfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\OLSAT.csv"

#read in and create dframes
dfS= pd.read_csv(Sfile,dtype='str')
dfM= pd.read_csv(Mfile,dtype='str')
dfP= pd.read_csv(Pfile,dtype='str')
dfOL= pd.read_csv(OLfile,dtype='str')

#merge to an output dfM

dfInter1=pd.merge(dfS, dfM, left_on='StudentID', right_on='StudentID')
dfInter2=pd.merge(dfInter1,dfOL, how='left', on='StudentID')
dfO=pd.merge(dfInter2, dfP, how = 'left', on=['StudentID','Discipline' ])
# write out the file - not enough memory to do it properly
Ofile=Ifile='C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\District93.csv'
dfO.to_csv(Ofile, index=False)   

