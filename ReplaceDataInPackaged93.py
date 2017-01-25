# Replaces the data extracts in a .twbx file
# Modified for CCSD93 which has 2 extract files
# arg[1] = .twbx file full path
# sys.argv[2]= new extract file 1 full path
# sys.argv[3]= new extract file 2 full path
# invoke python ReplaceDataInPackaged.py <file1> <file2> <file3>

import tempfile
import zipfile
import shutil
import os,sys
import ntpath


def remove_from_zip(zipfname, *filenames):
    tempdir = tempfile.mkdtemp()
    try:
        tempname = os.path.join(tempdir, 'new.zip')
        with zipfile.ZipFile(zipfname, 'r') as zipread:
            with zipfile.ZipFile(tempname, 'w') as zipwrite:
                for item in zipread.infolist():
                    if item.filename not in filenames:
                        data = zipread.read(item.filename)
                        zipwrite.writestr(item, data)
        shutil.move(tempname, zipfname)
    finally:
        shutil.rmtree(tempdir)

# main

TWBX_file = sys.argv[1]
Extract_file1 = sys.argv[2]
Extract_file2 = sys.argv[3]
print 'Replacing files:  ', ntpath.basename(Extract_file1),ntpath.basename(Extract_file2),'in workbook:  ',ntpath.basename(TWBX_file)
newnames=[]
#check for existence of both Extract_files and abort if not found
if(os.path.isfile(Extract_file1) and os.path.isfile(Extract_file2)):
    z=zipfile.ZipFile(TWBX_file,'r')
    names =z.namelist()
    for name in names:
        if (name.startswith('Data/')): 
            newnames.append(name)
            remove_from_zip(TWBX_file, name) #delete the old data files     
    with zipfile.ZipFile(TWBX_file, 'a') as z:
        for name in newnames:      
            if name.endswith('S.tde'): 
                z.write(Extract_file2,name) #add in grades extract
            else:      
                z.write(Extract_file1,name) #add in the assessment extract
        z.close()
else: print 'Extract File not found'
    
	
