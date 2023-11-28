@echo off

:: Checking Requirements...
echo Checking Requirements...
ping 127.0.0.1 >nul

:: Sets the modules required for the program to be ran
set modules=pygame,random,time,easing,soundmanager,configparser

:: Checks weather or not those modules are installed, and installs them if they arent
for /f "tokens=2 delims=:" %%a in ('python -c "import %modules%.*"') do 
  if exist %%~nxa goto : Found
  echo %%~nxa - Not Found
  echo Installing %%~nxa...
  pip install %%~nxa
  goto : Found

: Found
echo.

:: Prompts the user for what version of Quatro Tetris they want to run
echo.
echo Enter the Python version number to run (e.g., v0.0.1, v0.0.2): 
set /p quatro_version=

:: Tells the user what part of this file is running
echo.
echo Checking python version...
ping 127.0.0.1 >nul

:: Detects the type of python command you have installed on your system
if exist python goto : Python
if exist python3 goto : Python3
if exist py goto : ErrorPy

: Python
set python_command=python
goto :CheckPython

: Python3
set python_command=python3
goto :CheckPython

: ErrorPy
echo.
echo Error 0001
echo ---------------------
echo It appears as if you are using the 'py' command only as your python interpreter. Quatro Tetris is unable to run using the 'py' interpreter. Please install 'python' or 'python3'.
pause
exit /b 1

:CheckPython
python --version 2>&1 | findstr /i /r "^python" >nul
if errorlevel 1 goto : ErrorPython

:: Sets the filename based on the version selected by the user
set python_file=quatro-tetris-%quatro_version%.py

:: Detects the exact version of python the user is running and saves it to a variable
set python_version=!python --version 2>&1 | cut -d' ' -f2!

:: Clears the screen because the process was finished
echo.

:: Runs the game
if exist !python_file! goto : RunningGame
echo.
echo Error 0004
echo ---------------------
echo The Version of the game you are trying to run (!quatro_version!), does not exist or is not currently downloaded. Please ensure you downloaded the entire Quatro-Tetris folder from the repository, and that you typed the version number in correctly (v#.#.#)
pause
exit /b 1

: RunningGame
echo.
echo Running Quatro Tetris (!quatro_version!)
ping 127.0.0.1 >nul

set output=!python! !python_file! 2>&1
if !errorlevel! neq 0 goto : ErrorGame

:: Checks the exit code given by the game
if !output:~0,2! neq "Exit" goto : ErrorGame

:: Clears the screen because the process was finished
echo.

:: Runs the game
echo.
echo Quatro Tetris !quatro_version!
echo ---------------------
echo Thanks for playing
echo Give feedback on Twitter or Instagram by mentioning @zcraftelite
pause
exit /b 1

: ErrorGame
echo.
echo Error 0000
echo ---------------------
echo A unexpected error occurred. Please try again. If the issue persists, please contact the developer.
echo.
echo More Info
echo ---------------------
echo Game Version: !quatro_version!
echo Python Version: !python_version!
echo.
echo Python Output
echo ---------------------
echo !output!
pause
exit /b 1