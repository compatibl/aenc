@echo off

echo Switch to parent directory
pushd ..
echo.

set target=aenc
set level=""

echo Activate virtual environment
call venv\Scripts\activate.bat
echo.

echo Format using isort
isort %target% --sp=%level%.isort.cfg
echo.

echo Format using black
black %target% --config=%level%pyproject.toml --quiet
echo.

echo Validate using flake8
flake8 %target% --config=%level%.flake8
echo.

echo Deactivate virtual environment
call venv\Scripts\deactivate.bat
echo.

echo Return to original directory
popd
