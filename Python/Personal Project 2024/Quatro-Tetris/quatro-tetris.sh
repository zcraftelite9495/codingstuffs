#!/bin/bash

# Tells the user what part of this file is running
echo "Checking Requirements..."

# Sets the modules required for the program to be ran
modules=("pygame" "random" "time" "easing" "soundmanager" "configparser")

# Creates a progress bar
progress="$(progress -s 100 -w '[:bar]' -e '[:complete]' -d '[:eta]')"

# Checks weather or not those modules are installed, and installs them if they arent
for module in "${modules[@]}"; do
    if python -c "import $module" &>/dev/null; then
        echo "$module - Found"
        progress -c 10
    else
        echo "$module - Not Found"
        echo "Installing $module..."
        pip install $module
        progress -c 10
    fi
done

# Clears the progress bar
progress -c 0

# Prompts the user for what version of Quatro Tetris they want to run
read -p "Enter the Python version number to run (e.g., v0.0.1, v0.0.2): " quatro_version

# Detects the type of python command you have installed on your system
if command -v python &>/dev/null; then # Checks to see if you use 'python'
    python_command="python" # If you use 'python', sets the python command to 'python'
elif command -v python3 &>/dev/null; then # Checks to see if you use 'python3'
    python_command="python3" # If you use 'python3', sets the python command to 'python3'
elif command -v py &>/dev/null; then # Checks to see if you use 'py'
    # Spits out an error stating that the 'py' command is not compatible with this script
    echo "Error 0001"
    echo "----------------------"
    echo "It appears as if you are using the 'py' command only as your python interpreter. Quatro Tetris is unable to run using the 'py' interpreter. Please install 'python' or 'python3'."
    exit 1
elif command -v python2 &>/dev/null; then # Checks to see if you only have 'python2' installed
    # Spits out an error stating that Quatro Tetris cannot be run with Python 2
    echo "Error 0002"
    echo "----------------------"
    echo "It appears that you do not have a valid Python 3 command interpreter. Quatro Tetris is not able to be ran via Python 2. Please install a Python 3 Interpreter and try again."
    exit 1
else
    # Spits out an error stating the Quatro Tetris cannot be ran without Python
    echo "Error 0003"
    echo "----------------------"
    echo "It appears that you do not have a valid Python 3 command interpreter. Quatro Tetris cannot be run without Python 3. Please install a Python 3 Interpreter and try again."
fi

# Sets the filename based on the version selected by the user
python_file="quatro-tetris-$version.py"

# Detects the exact version of python the user is running and saves it to a variable
python_version=$($python_command --version 2>&1 | cut -d' ' -f2)

# Runs the game
if [ -f "$python_file" ]; then
    echo "Running Quatro Tetris ($version)"
    sleep 1
    clear
    # Gets the output given when the game exits
    output=$($python_command "$python_file" 2>&1)
    # Checks the exit code given by the game
    exit_code=$?
    if [ $exit_code -ne 0 ]; then # Checks if the exit was due to an error
        # If the exit was due to an error, the following error code is given
        if [[ $output =~ "SyntaxError" ]]; then
            echo "Error 0005"
            echo "----------------------"
            echo "A syntax error in the game code has occured. Please try again. If the issue presists, please contact the developer."
            echo ""
            echo "More Info"
            echo "----------------------"
            echo "Game Version: $version"
            echo "Python Version: $python_version"
            echo ""
            echo "Python Output"
            echo "----------------------"
            echo "$output"
            exit 1
        else
            clear
            echo "Error 0000"
            echo "----------------------"
            echo "A unexpected error in the game code has occured. Please try again. If the issue persists, please contact the developer."
            echo ""
            echo "More Info"
            echo "----------------------"
            echo "Game Version: $version"
            echo "Python Version: $python_version"
            echo ""
            echo "Python Output"
            echo "----------------------"
            echo "$output"
            exit 1
        fi
    fi
    sleep 1
    clear
    echo "Quatro Tetris $version"
    echo "----------------------"
    echo "Thanks for playing"
    echo "Give feedback on Twitter or Instagram by mentioning @zcraftelite"
    echo ""
else
    clear
    echo "Error 0004"
    echo "----------------------"
    echo "The Version of the game you are trying to run ($version), does not exist or is not currently downloaded. Please ensure you downloaded the entire Quatro-Tetris folder from the repository, and that you typed the version number in correctly (v#.#.#)"
    echo ""
    exit 1
fi