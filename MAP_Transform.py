# Transform the MAP file by (1) excluding fields that aren't needed and (2) pivoting the standards data
# so it can be handled properly by Tableau
# the list [cols] is a list of potentially useful fields, the ones I don't think I need are
# commented out
# From the original NWEA file the "NotSkipped" list is a list of the fields that are used.
# Input is the NWEA file that comes from the district
# The output file is MAP.csv
# full paths are hardwired
# invoke by python MAP_Transform.py <no args>
# Files are hardcoded.

import csv
# The desired columns for the dataframe are not commented out. The number in the
# comment is the actual column number in the NWEA file.
# They are enumerated in the list "Not Skipped"
# To add or remove a column from the transformed file, remove the comment and add
# the number of the column in the original file, starting the counting from 0

cols=['TermName',                           #0
'SchoolName',                               #2
'StudentID',                                #6
'Grade',                                     #10
'Discipline',                               #12
'TestRITScore',                             #24
'TestPercentile',                           #26
'GoalName',                                 # These are pivoted
'GoalRitScore',
'GoalStdErr',
'GoalRange',
'GoalAdjective',                
]
#column numbers where pivot happens
Pivot_Start=66
Pivot_End=105
NFields=5 #number of fields to pivot for each goal
Pivot_Range=range(Pivot_Start,Pivot_End)
#skipped columns
NotSkipped=[0,2,6,10,12,24,26]


MAPFile= "C:\Users\Elaine\Documents\BKL\CC93\RawData\NWEA Fall 16-17 Scores.csv"
Readfile=open(MAPFile,'rb')
reader=csv.reader(Readfile)

Outfile = "C:\Users\Elaine\Documents\BKL\CC93\RawData\MAP.csv"
Ofile= open(Outfile,'a+b')
wr=csv.writer(Ofile,delimiter=',')
wr.writerow(cols) #write header
rownum=0
for row in reader:
    if rownum==0: 
        head=row
    else:
        icolnum=0
        InitialOutRow=[]    #part of the output that isn't pivoted
        for col in row:
            if icolnum in NotSkipped and icolnum not in Pivot_Range:
                InitialOutRow.append(col)     
            icolnum+=1
#fixed folumns are set now produce the pivoted rows
    
        icolnum=Pivot_Start
        nfields=5
        ngoals=8
        for count in range(ngoals):
            CompleteOutRow=list(InitialOutRow)
            temp_list=[]
            for col in row[icolnum:icolnum+nfields]:
                if not not col:
                    CompleteOutRow.append(col)
            icolnum=icolnum+nfields
            if not not col: wr.writerow( CompleteOutRow)
#            print count,temp_list,len(CompleteOutRow)
    rownum+=1

