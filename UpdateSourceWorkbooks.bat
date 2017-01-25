REM ---Update the data fields in the source workbooks Initial4-5,Initial6-8, InitialK-3
REM --- Use this script when there are new fields in the views that the source workbooks will use
REM --- ReplaceData.bat will propogate the new vizes and the new data to the grade level dashboards
python ReplaceDataInPackaged.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\InitialK-3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr3.tde" 

python ReplaceDataInPackaged.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Initial4-5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr4.tde" 

python ReplaceDataInPackaged.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Initial6-8.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr7.tde"  
    