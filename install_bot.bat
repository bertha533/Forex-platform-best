@echo off
echo -------------------------------
echo Forex Bot Installer for Windows
echo -------------------------------

REM Step 1: Check for Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install it from https://www.python.org/downloads/
    pause
    exit /b
)

REM Step 2: Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Step 3: Activate environment
call venv\Scripts\activate.bat

REM Step 4: Upgrade pip
python -m pip install --upgrade pip

REM Step 5: Install required packages
pip install MetaTrader5 pandas numpy

echo -------------------------------------
echo ✅ Installation complete!
echo To run the bot, type:
echo     venv\Scripts\activate
echo     python bot.py
echo -------------------------------------
pause