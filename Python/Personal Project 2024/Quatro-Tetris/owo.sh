tasks=("task1" "task2" "task3" "task4" "task5" "task6" "task7")

custom_tasks=("Checking Linux Distribution" "Checking 'snap' version" "Checking Python version" "Verifying Python version" "Checking 'pygame' version" "Checking Requirements" "Checking Modules" "Checking Game Version")

function display_loading_tasks {
    for task in "${tasks[@]}" ; do
        custom_task=${custom_tasks[$task]}
        if [ "$task" = "done" ]; then
            echo "| ✓ | $custom_task"
        else
            echo "| - | $custom_task..."
        fi
    done
}

display_loading_tasks

task1="done"
display_loading_tasks 