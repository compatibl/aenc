@echo off

echo Switch to parent directory
pushd ..
echo.

:PROMPT
set AREYOUSURE=N
set /p AREYOUSURE=This will delete current venv and recreate it from scratch. Procced (Y\[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

echo Create empty venv
IF EXIST "venv" rd /s /q venv
python -m venv venv
echo.

echo Activate virtual environment
call venv\Scripts\activate.bat
echo.

echo Install requirements.txt
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

echo Deactivate virtual environment
call venv\Scripts\deactivate.bat
echo.

echo Return to original directory
popd
:END
