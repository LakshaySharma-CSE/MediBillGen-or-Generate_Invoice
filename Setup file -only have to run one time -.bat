@echo off
:: ======================================================
:: MediBillGen - Setup and Run Script by Lakshay Sharma
:: ======================================================

echo.
echo  Setting up MediBillGen environment...
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  Python is not installed! Please install Python 3.8 or above. 
    echo  Going to install python
    winget install Python.Python.3.14.0
)

if not exist venv (
    echo  Creating virtual environment...
    python -m venv venv
) else (
    echo  Virtual environment already exists.
)

call venv\Scripts\activate

echo  Upgrading pip...
python -m pip install --upgrade pip


echo  Installing dependencies...
pip install reportlab qrcode[pil]

echo.
pause
