@echo off

:: Checking Requirements...

:: Set modules required for the program to be ran
set modules=("pygame" "random" "time" "easing" "soundmanager" "configparser")

:: Checks weather or not those modules are installed, and installs them if they arent
for /f "tokens=2 delims=:" %%m in (' свободн命令 python -c "import %modules%" ^| command') do (
  echo %%m - Found
) else (
  echo %%m - Not Found
  echo Installing %%m...
  pip install %%m
)

:: Prompts the user for what version of Quatro Tetris they want to run
set /p quatro_version=Enter the Python version number to run (e.g., v0.0.1, v0.0.2): 

:: Detects the type of python command you have installed on your system
if exist python (
  set python_command=python
) else if exist python3 (
  set python_command=python3
) else if exist py (
  echo Error 0001
  echo --------------------
  echo It appears as if you are using the 'py' command only as your python interpreter. Quatro Tetris is unable to run using the 'py' interpreter. Please install 'python' or 'python3'.
  exit /b 1
) else (
  echo Error 0002
  echo --------------------
  echo It appears that you do not have a valid Python 3 command interpreter. Quatro Tetris is not able to be ran via Python 2. Please install a Python 3 Interpreter and try again.
  exit /b 1
)

:: Sets the filename based on the version selected by the user
set python_file=quatro-tetris-%quatro_version%.py

:: Detects the exact version of python the user is running and saves it to a variable
for /f "tokens=2 delims=:" %%v in ('python --version 2^>nul ^| cut -d" " -f2') do (
  set python_version=%%v
)

:: Runs the game
if exist %python_file% (
  echo Running Quatro Tetris (%quatro_version%)
  ping 127.0.0.1 -n 1 >nul
  clear
  rem Gets the output given when the game exits
  set output=!python_command! %python_file% 2^>nul
  rem Checks the exit code given by the game
  set exit_code=!errorlevel!
  if !exit_code! neq 0 (
      rem If the exit was due to an error, the following error code is given
      clear
      echo Error 0000
      echo --------------------
      echo A unexpected error occured. Please try again. If the issue persists, please contact the developer.
      echo !exit_code!
      echo !python_version!
      echo !output!
      exit /b 1
  )
  ping 127.0.0.1 -n 1 >nul
  clear
  echo Quatro Tetris %quatro_version%
  echo --------------------
  echo Thanks for playing
  echo Give feedback on Twitter or Instagram by mentioning @zcraftelite
  echo !exit_code!
else (
  clear
  echo Error 0004
  echo --------------------
  echo The Version of the game you are trying to run (!quatro_version!), does not exist or is not currently downloaded. Please ensure you downloaded the entire Quatro-Tetris folder from the repository, and that you typed the version number in correctly (v#.#.#)
  echo !exit_code!
  exit /b 1
  )
)