# Join student data with MAP assessment data
#File: CreateExtract1
#Purpose: generate school,grade .csv files and extracts
#Output:  <school><gradelevel>.csv (42 files)

import dataextract as tde
import pandas as pd
import csv,gc

def create_extract():
  
    tableDef = tde.TableDefinition()
    tableDef.addColumn('Last_Name', tde.Type.CHAR_STRING)
    tableDef.addColumn('First_name', tde.Type.CHAR_STRING)
    tableDef.addColumn('Grade_Level', tde.Type.CHAR_STRING)
    tableDef.addColumn('SchoolID', tde.Type.CHAR_STRING)
    tableDef.addColumn('Ethnicity', tde.Type.CHAR_STRING)
    tableDef.addColumn('Gender', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_504', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Accelerated_Placement', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Accelerated_Subjects', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Dual_Language', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Mentor_Program', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Misc_Group', tde.Type.CHAR_STRING)
 #   tableDef.addColumn('93_Reading_Support', tde.Type.CHAR_STRING)
    tableDef.addColumn('Local Demographic', tde.Type.CHAR_STRING)
    tableDef.addColumn('Membership', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_IEP', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_LEP', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_LII', tde.Type.CHAR_STRING)
    tableDef.addColumn('Course_Name', tde.Type.CHAR_STRING)
    tableDef.addColumn('Teacher', tde.Type.CHAR_STRING)
    tableDef.addColumn('TermName', tde.Type.CHAR_STRING)
    tableDef.addColumn('SchoolName', tde.Type.CHAR_STRING)
    tableDef.addColumn('StudentID', tde.Type.CHAR_STRING)
    tableDef.addColumn('Discipline', tde.Type.CHAR_STRING)
    tableDef.addColumn('TestRITScore',tde.Type.INTEGER)
    tableDef.addColumn('TestPercentile',tde.Type.INTEGER)
    tableDef.addColumn('GoalName', tde.Type.CHAR_STRING)
    tableDef.addColumn('GoalRitScore',tde.Type.INTEGER)
    tableDef.addColumn('GoalStdErr', tde.Type.CHAR_STRING)
    tableDef.addColumn('GoalRange', tde.Type.CHAR_STRING)
    tableDef.addColumn('GoalAdjective', tde.Type.CHAR_STRING)
    tableDef.addColumn('PARCC_Score', tde.Type.CHAR_STRING)
    tableDef.addColumn('PARCC_PrfLvl', tde.Type.CHAR_STRING)
    tableDef.addColumn('93_District_Entry_Year', tde.Type.CHAR_STRING)
    tableDef.addColumn('SAI_Total', tde.Type.CHAR_STRING)
    tableDef.addColumn('SAI_Verbal', tde.Type.CHAR_STRING)
    tableDef.addColumn('SAI_NonVerbal', tde.Type.CHAR_STRING)  
    
    table=tdefile.addTable('Extract',tableDef)
    newrow = tde.Row(tableDef)
    for index,row in df1.iterrows():
   
        newrow.setCharString(0, str(row['Last_Name']))
        newrow.setCharString(1, str(row['First_Name']))
        newrow.setCharString(2, str(row['Grade_Level']))
        newrow.setCharString(3, str(row['SchoolID']))
        newrow.setCharString(4, str(row['Ethnicity']))
        newrow.setCharString(5, str(row['Gender']))
        newrow.setCharString(6, str(row['Local Demographic']))
        newrow.setCharString(7, str(row['Membership']))
        newrow.setCharString(8, str(row['IL_IEP']))
        newrow.setCharString(9, str(row['IL_LEP']))
        newrow.setCharString(10, str(row['IL_LII']))
        newrow.setCharString(11, str(row['Course_Name']))
        newrow.setCharString(12, str(row['Teacher']))
        newrow.setCharString(13, str(row['TermName']))
        newrow.setCharString(14, str(row['SchoolName']))
        newrow.setCharString(15, str(row['StudentID']))
        newrow.setCharString(16, str(row['Discipline']))
        newrow.setInteger(17, int(row['TestRITScore']))
        newrow.setInteger(18, int(row['TestPercentile']))
        newrow.setCharString(19, str(row['GoalName']))
        newrow.setInteger(20, int(row['GoalRitScore']))
        newrow.setCharString(21, str(row['GoalStdErr']))
        newrow.setCharString(22, str(row['GoalRange']))
        newrow.setCharString(23, str(row['GoalAdjective']))
        newrow.setCharString(24, str(row['PARCC_Score']))
        newrow.setCharString(25, str(row['PARCC_PrfLvl']))
        newrow.setCharString(26, str(row['93_District_Entry_Year']))
        newrow.setCharString(27, str(row['SAI_Total']))
        newrow.setCharString(28, str(row['SAI_Verbal']))
        newrow.setCharString(29, str(row['SAI_NonVerbal']))
        table.insert(newrow)
    tdefile.close()       
    return


GrName={'1':'Gr1','2':'Gr2','3':'Gr3','4':'Gr4','5':'Gr5','6':'Gr6','7':'Gr7','8':'Gr8','K':'GrK'}
ScName={'2001':'CS','2011':'CL','2007':'EJ','2010':'HL','2009':'JS','2004':'RD','1004':'ST','2006':'WT'}
output_root ="C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\\"
#extensions:
tde_ext='.tde'
csv_ext='.csv'
Ifile='C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\District93.csv'
dfO= pd.read_csv(Ifile,dtype='str')

# write out all the school files
for school in ScName:  
       for gradeName in GrName:
           df1=dfO.loc[(dfO['SchoolID'] == school) & (dfO['Grade_Level'] == gradeName)]
           if not df1.empty: 
               file = output_root+ScName[school]+GrName[gradeName]
               print 'Creating file: ', file
               df1[['TestRITScore','TestPercentile','GoalRitScore']]=df1[['TestRITScore','TestPercentile','GoalRitScore']].apply(pd.to_numeric)
               tdefile=tde.Extract(file+tde_ext)
               create_extract()
               df1.to_csv(file+csv_ext)


