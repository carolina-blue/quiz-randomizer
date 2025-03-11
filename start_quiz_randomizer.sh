#!/bin/bash
echo "Starting Quiz Randomizer..."
python3 start_quiz_randomizer.py
if [ $? -ne 0 ]; then
    echo
    echo "An error occurred. Please make sure Python is installed."
    echo
    read -p "Press Enter to exit..."
fi 