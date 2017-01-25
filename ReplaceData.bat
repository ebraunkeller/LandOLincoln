REM -------------------------------- BEGIN UPDATE ----------------------------------(C) 2016-2017 BKLSchoolVision --------------
REM --- Do the copy from the initial one once. Thereafter, delete the copies and just update the individual workbooks
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Carol Stream Grade 1.twbx","Carol Stream Grade 2.twbx","Carol Stream Grade 3.twbx","Carol Stream Grade 4.twbx","Carol Stream Grade 5.twbx"
(FOR %%A IN ("Carol Stream Grade 1.twbx","Carol Stream Grade 2.twbx","Carol Stream Grade 3.twbx",) DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Carol Stream Grade 4.twbx","Carol Stream Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr2.tde"  "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr3S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr4S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGr5S.tde"    

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Carol Stream Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGrK.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CSGrKS.tde"

REM -----------------------------------------------------------------------------------------------------------------    
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Cloverdale Grade 1.twbx","Cloverdale Grade 2.twbx","Cloverdale Grade 3.twbx","Cloverdale Grade 4.twbx","Cloverdale Grade 5.twbx"
(FOR %%A IN ("Cloverdale Grade 1.twbx","Cloverdale Grade 2.twbx","Cloverdale Grade 3.twbx") DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Cloverdale Grade 4.twbx","Cloverdale Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr1K.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGrKS.tde"
    
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr2.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr3S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr4S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Cloverdale Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\CLGr5S.tde"    
REM ----------------------------------------------------------------------------------------------------------------------------    
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Elsie Johnson Grade 1.twbx","Elsie Johnson Grade 2.twbx","Elsie Johnson Grade 3.twbx","Elsie Johnson Grade 4.twbx","Elsie Johnson Grade 5.twbx"
(FOR %%A IN ("Elsie Johnson Grade 1.twbx","Elsie Johnson Grade 2.twbx","Elsie Johnson Grade 3.twbx") DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Elsie Johnson Grade 4.twbx","Elsie Johnson Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGrK.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGrKS.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr2.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr3S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr4S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Elsie Johnson Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\EJGr5S.tde"    
    
REM ---------------------------------------------------------------------------------------------------------------------
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Heritage Lakes Grade 1.twbx","Heritage Lakes Grade 2.twbx","Heritage Lakes Grade 3.twbx","Heritage Lakes Grade 4.twbx","Heritage Lakes Grade 5.twbx"
(FOR %%A IN ("Heritage Lakes Grade 1.twbx","Heritage Lakes Grade 2.twbx","Heritage Lakes Grade 3.twbx") DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Heritage Lakes Grade 4.twbx","Heritage Lakes Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGrK.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGrKS.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr2.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr3S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr4S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Heritage Lakes Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\HLGr5S.tde"  
 
REM -----------------------------------------------------------------------------------------
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Roy Deshane Grade 1.twbx","Roy Deshane Grade 2.twbx","Roy Deshane Grade 3.twbx","Roy Deshane Grade 4.twbx","Roy Deshane Grade 5.twbx"
(FOR %%A IN ("Roy Deshane Grade 1.twbx","Roy Deshane Grade 2.twbx","Roy Deshane Grade 3.twbx") DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Roy Deshane Grade 4.twbx","Roy Deshane Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGrK.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGrKS.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr2.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr3S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr4S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Roy Deshane Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\RDGr5S.tde"  

REM ------------------------------------------------------------------------------------------------------------
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Western Trails Grade 1.twbx","Western Trails Grade 2.twbx,"Western Trails Grade 3.twbx","Western Trails Grade 4.twbx","Western Trails Grade 5.twbx"
(FOR %%A IN ("Western Trails Grade 1.twbx","Western Trails Grade 2.twbx","Western Trails Grade 3.twbx") DO COPY InitialK-3.twbx %%A)
(FOR %%A IN ("Western Trails Grade 4.twbx","Western Trails Grade 5.twbx") DO COPY Initial4-5.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade K.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr1S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade 1.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr1.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr1S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade 2.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr2.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr2S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade 3.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr3.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr3S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade 4.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr4.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr4S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Western Trails Grade 5.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr5.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\WTGr5S.tde"  

REM --------------------------------------------------------------------------------------------
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Jay Stream Grade 6.twbx","Jay Stream Grade 7.twbx","Jay Stream Grade 8.twbx"
(FOR %%A IN ("Jay Stream Grade 6.twbx","Jay Stream Grade 7.twbx","Jay Stream Grade 8.twbx") DO COPY Initial6-8.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Jay Stream Grade 6.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr6.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr6S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Jay Stream Grade 7.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr7.tde"  "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr7S.tde"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Jay Stream Grade 8.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr8.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\JSGr8S.tde"
REM ----------------------------------------------------------------------------------------------
cd "c:\users\elaine\documents\my tableau repository\workbooks\ccsd93"
del "Stratford Grade 6.twbx","Stratford Grade 7.twbx","Stratford Grade 8.twbx"
(FOR %%A IN ("Stratford Grade 6.twbx","Stratford Grade 7.twbx","Stratford Grade 8.twbx") DO COPY Initial6-8.twbx %%A)
cd "c:\users\elaine\documents\bkl\cc93\scripts"

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Stratford Grade 6.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr6.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr6S.tde"
 
python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Stratford Grade 7.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr7.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr7S.tde" 

python ReplaceDataInPackaged93.py "C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\CCSD93\Stratford Grade 8.twbx" ^
	"C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr8.tde" "C:\Users\Elaine\Documents\BKL\CC93\TableauFormat\STGr8S.tde"



