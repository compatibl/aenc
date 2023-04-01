@echo off

pushd ..

echo.
echo Activate virtual environment
call venv\Scripts\activate.bat

echo.
echo Delete build, egg-info, and dist directories before building
if exist aenc.egg-info rmdir/q/s aenc.egg-info
if exist build rmdir/q/s build
if exist dist rmdir/q/s dist

echo.
echo Build wheel
python setup.py bdist_wheel

echo.
echo Delete build and egg-info directories after building, wheel is located in dist
if exist aenc.egg-info rmdir/q/s aenc.egg-info
if exist build rmdir/q/s build

echo.
echo Exit without deactivating virtual environment

popd
