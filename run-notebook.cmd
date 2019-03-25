REM - Place this file in the root of your notebook folders
REM - Double-click to run the jupyter notebook
REM - the python path search will then include steel-design lib folder

REM - set the following line to point to the root of the 'ca-steel-design' tree
set casd=%cd%\..\ca-steel-design
set PYTHONPATH=%casd%\lib;%PYTHONPATH%

REM - perhaps modify this line for the location of your Python
C:\Anaconda3\python.exe -m jupyter notebook

REM - or:
REM C:\Anaconda3\python.exe -m jupyter lab
