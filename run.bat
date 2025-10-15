@echo off
REM File Integrity Checker - Launch Script for Windows
REM Double-click this file to run the application

echo ========================================
echo   File Integrity Checker
echo   Starting application...
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher from python.org
    pause
    exit /b 1
)

REM Display Python version
echo Python found:
python --version
echo.

REM Run the application
echo Launching File Integrity Checker...
echo.
python app_gui.py

REM If there's an error, keep window open
if errorlevel 1 (
    echo.
    echo ========================================
    echo   An error occurred!
    echo ========================================
    pause
)
