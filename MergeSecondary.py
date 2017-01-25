# CCSD93 student achievement dashboard data. Exactly the same as the main dashboard
# except that MAP and PARCC are replaced by "Standards Achievement"
# So this will create a secondary extract file which runs in a new dashboard.
#Purpose: Join student data and standard assessment data).Create the district and all the school/grade level files by df.loc method
#Input: Students.csv (generated) StandardAssessment<><><>.csv download from district
#Output: District93.csv, <school><gradelevel>S.csv (42 files) and tde
#Creates a second data extract for second dashboard appended with letter S (for standard)
import dataextract as tde
import pandas as pd
import csv
def create_extract():
  
    tableDef = tde.TableDefinition()
    tableDef.addColumn('Last_Name', tde.Type.CHAR_STRING)
    tableDef.addColumn('First_name', tde.Type.CHAR_STRING)
    tableDef.addColumn('Grade_Level', tde.Type.CHAR_STRING)
    tableDef.addColumn('SchoolID', tde.Type.CHAR_STRING)
    tableDef.addColumn('Ethnicity', tde.Type.CHAR_STRING)
    tableDef.addColumn('Gender', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_504', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Accelerated_Placement', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Accelerated_Subjects', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Dual_Language', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Mentor_Program', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Misc_Group', tde.Type.CHAR_STRING)
#    tableDef.addColumn('93_Reading_Support', tde.Type.CHAR_STRING)
    tableDef.addColumn('Local Demographic', tde.Type.CHAR_STRING)
    tableDef.addColumn('Membership', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_IEP', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_LEP', tde.Type.CHAR_STRING)
    tableDef.addColumn('IL_LII', tde.Type.CHAR_STRING)
    tableDef.addColumn('Course_Name', tde.Type.CHAR_STRING)
    tableDef.addColumn('Teacher', tde.Type.CHAR_STRING)
    tableDef.addColumn('93_District_Entry_Year', tde.Type.CHAR_STRING)
#   tableDef.addColumn('93_Math_Services', tde.Type.CHAR_STRING)
#   tableDef.addColumn('93_Gifted_Placement', tde.Type.CHAR_STRING)
    tableDef.addColumn('NAME', tde.Type.CHAR_STRING)
    tableDef.addColumn('STORECODE', tde.Type.CHAR_STRING)
    tableDef.addColumn('SCORE', tde.Type.CHAR_STRING)  
    tableDef.addColumn('SUBJECTAREA', tde.Type.CHAR_STRING)  
    
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
#       newrow.setCharString(6, str(row['93_504']))
#       newrow.setCharString(7, str(row['93_Accelerated_Placement']))
#       newrow.setCharString(8, str(row['93_Accelerated_Subjects']))
#       newrow.setCharString(9, str(row['93_Dual_Language']))
#       newrow.setCharString(10, str(row['93_Mentor_Program']))
#       newrow.setCharString(11, str(row['93_Misc_Group']))
#       newrow.setCharString(12, str(row['93_Reading_Support']))
        newrow.setCharString(8, str(row['IL_IEP']))
        newrow.setCharString(9, str(row['IL_LEP']))
        newrow.setCharString(10, str(row['IL_LII']))
        newrow.setCharString(11, str(row['Course_Name']))
        newrow.setCharString(12, str(row['Teacher']))   
        newrow.setCharString(13, str(row['93_District_Entry_Year']))
#        newrow.setCharString(15, str(row['93_Math_Services']))
#        newrow.setCharString(16, str(row['93_Gifted_Placement']))
        newrow.setCharString(14, str(row['NAME']))
        newrow.setCharString(15, str(row['STORECODE']))
        newrow.setCharString(16, str(row['SCORE']))
        newrow.setCharString(17, str(row['SUBJECTAREA']))
        table.insert(newrow)
    tdefile.close()       
    return
GrName={'1':'Gr1S','2':'Gr2S','3':'Gr3S','4':'Gr4S','5':'Gr5S','6':'Gr6S','7':'Gr7S','8':'Gr8S','0':'GrKS'}
ScName={'2001':'CS','2011':'CL','2007':'EJ','2010':'HL','2009':'JS','2004':'RD','1004':'ST','2006':'WT'}
output_root ="C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\\"
#extensions:
tde_ext='.tde'
csv_ext='.csv'

Sfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\Students.csv"
Gfile="C:\Users\Elaine\Documents\BKL\CC93\RawData\Grades.csv"
dfS= pd.read_csv(Sfile,dtype='str')
dfG= pd.read_csv(Gfile,dtype='str')
for school in ScName:
    for grade in GrName:
        dfS1=dfS.loc[(dfS['SchoolID'] == school) & (dfS['Grade_Level'] == grade)]
        dfG1=dfG.loc[(dfG['SCHOOLID'] == school) & (dfG['GRADE_LEVEL'] == grade)]
        df1=pd.merge(dfS1,dfG1, left_on='StudentID', right_on='StudentID')
        print '******************************'
# write out all the school files
        if not df1.empty: 
            file = output_root+ScName[school]+GrName[grade]
            print 'Creating file: ', file
            tdefile=tde.Extract(file+tde_ext)
            create_extract()
            df1.to_csv(file+csv_ext)