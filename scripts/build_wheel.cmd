@echo off

echo Switch to parent directory
pushd ..
echo.

echo Cleanup existing artifacts
IF EXIST "build" rd /s /q build
IF EXIST "dist" rd /s /q dist
IF EXIST "aenc.egg-info" rd /s /q "aenc.egg-info"
echo.

echo Activate virtual environment
call venv\Scripts\activate.bat
echo.

echo Install setup-related packages in venv
python -m pip install --upgrade pip
pip install setuptools wheel
echo.

echo Create wheel
python setup.py bdist_wheel
echo.

echo Deactivate virtual environment
call venv\Scripts\deactivate.bat
echo.

echo Return to original directory
popd
