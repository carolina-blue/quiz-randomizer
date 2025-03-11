# Quiz Randomizer Installation Guide

This guide will help you install and run the Quiz Randomizer Tool on your computer.

## Prerequisites

Before installing Quiz Randomizer, you need to have Python installed on your computer.

### Installing Python

1. **For Windows users:**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"
   - Complete the installation

2. **For Mac users:**
   - Python comes pre-installed on most Macs
   - For best results, you can download the latest version from [python.org](https://www.python.org/downloads/)

## Running Quiz Randomizer

### Windows Users

1. Extract all the files from the zip archive to a folder of your choice
2. Double-click `start_quiz_randomizer.bat`
3. The first time you run it, it may take a moment to install the required dependencies

### Mac Users

1. Extract all the files from the zip archive to a folder of your choice
2. Open Terminal (from Applications > Utilities)
3. Navigate to the folder where you extracted the files:
   ```
   cd /path/to/QuizRandomizer
   ```
4. Make the start script executable (if not already):
   ```
   chmod +x start_quiz_randomizer.sh
   ```
5. Run the script:
   ```
   ./start_quiz_randomizer.sh
   ```
6. Alternatively, you can directly run:
   ```
   python3 start_quiz_randomizer.py
   ```

## Manual Installation (if automatic installation fails)

If the automatic dependency installation fails, you can install them manually:

1. Open a command prompt (Windows) or Terminal (Mac)
2. Navigate to the Quiz Randomizer folder
3. Run:
   ```
   pip install -r requirements.txt
   ```
   (On Mac, you might need to use `pip3` instead of `pip`)

## Troubleshooting

- **"Python is not recognized as an internal or external command"** (Windows): Make sure Python is added to your PATH
- **Missing modules or libraries**: Run `pip install -r requirements.txt` to install all dependencies
- **Permission errors** (Mac): Make sure the script is executable (`chmod +x start_quiz_randomizer.sh`)

If you encounter any other issues, please report them on GitHub. 