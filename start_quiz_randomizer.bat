@echo off
echo Starting Quiz Randomizer...
python start_quiz_randomizer.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred. Please make sure Python is installed and in your PATH.
    echo.
    pause
) 