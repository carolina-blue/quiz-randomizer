#!/usr/bin/env python3
"""
Quiz Randomizer Launcher

This script provides an easy way to launch the Quiz Randomizer tool.
"""

import tkinter as tk
import os
import sys
import subprocess
import platform

def check_dependencies():
    """Check if all required dependencies are installed."""
    try:
        import fpdf
        import docx
        import yaml
        import striprtf
        return True
    except ImportError as e:
        return False

def install_dependencies():
    """Install missing dependencies using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Main launcher function."""
    print("Starting Quiz Randomizer Tool...")
    
    if not check_dependencies():
        print("Some dependencies are missing. Attempting to install them...")
        if not install_dependencies():
            print("Failed to install dependencies. Please install them manually.")
            print("Run: pip install -r requirements.txt")
            input("Press Enter to exit...")
            return
    
    try:
        # Import and run the main application
        from quiz_randomizer import main
        main()
    except Exception as e:
        print(f"Error starting Quiz Randomizer: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 