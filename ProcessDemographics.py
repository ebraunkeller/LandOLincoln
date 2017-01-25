# This file picks out the usefull fields from the ClassList file and the Demographics file provided
# by the district and joins them using Pandas to provide files for each grade and school that  contains student demographics
# and courses in one file
# Non descriptive fields (eg 1,0) are replaced by descriptive fields (eg Not ELL) and blank fields
# are replaced by 'No', so that it doesn't have to be done in Tableau.
# To clean up the database, YES,Yes,yes, Y are replaced by Yes, and NO, No, no, N are replaced by No
# input files are "../RawData/Class Roster.csv" and "../RawData/Demographics.csv" which come fromthe district.
# output is Students.csv
# This file will be joined with the assessment file "MAP.csv" in "MergePrimary.py"to be used by Tableau for the assessment
# dashboard

import pandas as pd
import csv

ethnic_dict = {'11':'Hispanic/Latino',
               '12': 'Native American',
               '13':'Asian',
               '14':'Black',
               '15':'Native Hawaiian',
               '16':'White',
               '17':'Multi'}
lep_dict = {None: 'Not ELL', '1': 'ELL'}
iep_dict = {None: 'Not SPED','1': 'SPED'}
lin_dict = {None: 'Not LI','1': 'LI'}
dict={None: 'No','Y':'Yes','yes':'Yes','N':'No','no':'No','YES':'Yes','NO':'No'}

# Choose the desired columns from each file
Class_Cols=['Student_Number','Course_Name','Teacher']
Demo_Cols=['Student_Number','Last_Name','First_Name','Grade_Level','SchoolID','Ethnicity','Gender',
           'IL_IEP','IL_LEP','IL_LII',
           '93_504','93_Accelerated_Placement','93_Accelerated_Subjects','93_Advanced_Placement',
           '93_AdvancedMath','93_Dual_Language','93_Mentor_Program','93_Reading_Support','93_District_Entry_Year',
           '93_Math_Services','93_Gifted_Placement']
           
# identify columns for melt - these are not melted
ID_VARS=['Student_Number','Last_Name','First_Name','Grade_Level','SchoolID','Course_Name','Teacher','Ethnicity','Gender',
        'IL_IEP','IL_LEP','IL_LII','93_District_Entry_Year']
# Pivoted column names
VAR_NAME='Local Demographic'
VALUE_NAME='Membership'

#Absolute path to files           
ClassRosterFile = "C:\Users\Elaine\Documents\BKL\CC93\RawData\Class Roster.csv"
DemographicsFile= "C:\Users\Elaine\Documents\BKL\CC93\RawData\Demographics.csv"
Outfile='C:\Users\Elaine\Documents\BKL\CC93\RawData\Students.csv'
# Read .csv file into df
dfCR= pd.read_csv(ClassRosterFile,dtype='str')
#rename and select the columns
dfCR.columns=['Student_Number','First_Name','Last_Name','Course_Name','Grade_Level','Teacher','Expression','SchoolID','TermID']
dfCR_New=dfCR[Class_Cols]
# open the demographics file to a dataframe and change (1,0) codes with real meanings
dfDemoInit=pd.read_csv(DemographicsFile,dtype='str')

dfDemoInit.Ethnicity=dfDemoInit.Ethnicity.replace(ethnic_dict)
dfDemoInit.IL_LEP=dfDemoInit.IL_LEP.replace(lep_dict)
dfDemoInit.IL_IEP=dfDemoInit.IL_IEP.replace(iep_dict)
dfDemoInit.IL_LII=dfDemoInit.IL_LII.replace(lin_dict)
#clean up the empty fields
dfDemoInit = dfDemoInit.replace(dict)
#select fields
dfDemoFinal=dfDemoInit[Demo_Cols]


#join the dataframss by student number and melt down the demographic groups
dfStudents1 = pd.merge(dfDemoFinal,dfCR_New, on='Student_Number')
dfStudents  = pd.melt(dfStudents1, id_vars=ID_VARS,var_name=VAR_NAME,value_name=VALUE_NAME)
dfStudents.rename(columns={'Student_Number':'StudentID'},inplace=True)
dfStudents.to_csv(Outfile,index=False)