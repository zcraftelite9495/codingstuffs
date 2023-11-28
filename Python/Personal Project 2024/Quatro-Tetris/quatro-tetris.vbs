' Checking Requirements...
echo "Checking Requirements..."
Wscript.Sleep 1000

' Sets the modules required for the program to be ran
Dim modules : modules = Array("pygame", "random", "time", "easing", "soundmanager", "configparser")

' Checks weather or not those modules are installed, and installs them if they arent
For Each module In modules
  If Not python.IsModuleInstalled(module) Then
      echo module & "- Not Found"
      echo "Installing " & module & "..."
      pip.Install(module)
  Else
      echo module & "- Found"
  End If
Next

' Clears the screen because the process was finished
clear

' Prompts the user for what version of Quatro Tetris they want to run
Dim quatro_version : quatro_version = InputBox("Enter the Python version number to run (e.g., v0.0.1, v0.0.2): ", "Quatro Tetris")
clear

' Tells the user what part of this file is running
echo "Checking python version..."
Wscript.Sleep 1000

' Detects the type of python command you have installed on your system
If python.IsCommandAvailable("python") Then
  python_command = "python"
ElseIf python.IsCommandAvailable("python3") Then
  python_command = "python3"
ElseIf python.IsCommandAvailable("py") Then
  ' Spits out an error stating that the 'py' command is not compatible with this script
  echo "Error 0001"
  echo "----------------------"
  echo "It appears as if you are using the 'py' command only as your python interpreter. Quatro Tetris is unable to run using the 'py' interpreter. Please install 'python' or 'python3'."
  Wscript.Quit 1
Else
  ' Spits out an error stating that Quatro Tetris cannot be run without Python
  echo "Error 0003"
  echo "----------------------"
  echo "It appears that you do not have a valid Python 3 command interpreter. Quatro Tetris cannot be run without Python 3. Please install a Python 3 Interpreter and try again."
  Wscript.Quit 1
End If

' Clears the screen because the process was finished
clear

' Tells the user what part of this file is running
echo "Checking game version..."
Wscript.Sleep 500

' Sets the filename based on the version selected by the user
python_file = "quatro-tetris-" & quatro_version & ".py"

' Detects the exact version of python the user is running and saves it to a variable
python_version = python.GetVersion()

' Clears the screen because the process was finished
clear

' Runs the game
If File.Exists(python_file) Then
  echo "Running Quatro Tetris (" & quatro_version & ")"
  Wscript.Sleep 1000
  clear
  Dim output : output = python.Run(python_command, python_file, 2)
  Dim exit_code : exit_code = Wscript.GetExitCode()
  If exit_code <> 0 Then
      ' If the exit was due to an error, the following error code is given
      clear
      echo "Error 0000"
      echo "----------------------"
      echo "A unexpected error occured. Please try again. If the issue persists, please contact the developer."
      echo ""
      echo "More Info"
      echo "----------------------"
      echo "Game Version: " & quatro_version
      echo "Python Version: " & python_version
      echo ""
      echo "Python Output"
      echo "----------------------"
      echo output
      Wscript.Quit 1
  End If
  Wscript.Sleep 1000
  clear
  echo "Quatro Tetris " & quatro_version & " "
  echo "----------------------"
  echo "Thanks for playing"
  echo "Give feedback on Twitter or Instagram by mentioning @zcraftelite"
  echo ""
  Wscript.Quit 1
Else
  clear
  echo "Error 0004"
  echo "----------------------"
  echo "The Version of the game you are trying to run (" & quatro_version & "), does not exist or is not currently downloaded. Please ensure you downloaded the entire Quatro-Tetris folder from the repository, and that you typed the version number in correctly (v#.#.#)"
  echo ""
  Wscript.Quit 1
End If

' Clears the screen because the process was finished
clear