# upload all the dashboards to CCSD93 google drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload(id,file):
    print file, id
    try:
        gfile = drive.CreateFile({'title':file,"parents": [{"kind": "drive#fileLink","id": id}]})
        gfile.SetContentFile(local_direct +file)
        gfile.Upload()
        print 'File uploaded: ',file
    except: print 'File not found   ',file
    
# source directory
local_direct= 'c:\\Users\\Elaine\\Documents\\My Tableau Repository\\Workbooks\\CCSD93\\'

#destination directories
directories= ('Carol_Stream',
             'Cloverdale',
             'District',
             'Elsie_Johnson',
             'Heritage_Lakes',
             'Jay_Stream',
             'Roy_Deshane',
             'Stratford',
             'Western_Trails'
              )


CCSD93files =(
'Carol_Stream Grade K.twbx',
'Carol Stream Grade 1.twbx',
'Carol Stream Grade 2.twbx',
'Carol Stream Grade 3.twbx',
'Carol Stream Grade 4.twbx',
'Carol Stream Grade 5.twbx',
'Cloverdale Grade K.twbx',
'Cloverdale Grade 1.twbx',
'Cloverdale Grade 2.twbx',
'Cloverdale Grade 3.twbx',
'Cloverdale Grade 4.twbx',
'Cloverdale Grade 5.twbx',
'Elsie Johnson Grade K.twbx',
'Elsie Johnson Grade 1.twbx',
'Elsie Johnson Grade 2.twbx',
'Elsie Johnson Grade 3.twbx',
'Elsie Johnson Grade 4.twbx',
'Elsie Johnson Grade 5.twbx',
'Heritage Lakes Grade K.twbx',
'Heritage Lakes Grade 1.twbx',
'Heritage Lakes Grade 2.twbx',
'Heritage Lakes Grade 3.twbx',
'Heritage Lakes Grade 4.twbx',
'Heritage Lakes Grade 5.twbx',
'Jay Stream Grade 6.twbx',
'Jay Stream Grade 7.twbx',
'Jay Stream Grade 8.twbx',
'Roy Deshane Grade K.twbx',
'Roy Deshane Grade 1.twbx',
'Roy Deshane Grade 2.twbx',
'Roy Deshane Grade 3.twbx',
'Roy Deshane Grade 4.twbx',
'Roy Deshane Grade 5.twbx',
'Stratford Grade 6.twbx',
'Stratford Grade 7.twbx',
'Stratford Grade 8.twbx',
'Western Trails Grade K.twbx',
'Western Trails Grade 1.twbx',
'Western Trails Grade 2.twbx',
'Western Trails Grade 3.twbx',
'Western Trails Grade 4.twbx',
'Western Trails Grade 5.twbx'
)

gauth=GoogleAuth()
gauth.LocalWebserverAuth() #creates local webserver and auto handles authentication
drive= GoogleDrive(gauth)

file_list = drive.ListFile({'q': "trashed=false"}).GetList()
for file in file_list:

    if file['title'] in directories: # one of the CCSd93 directories
        direct=file['title']
        for localfile in CCSD93files:
            if localfile.startswith(direct[:3]): # match the directory with the file name start
                upload(file['id'],localfile)

            
            
            
            