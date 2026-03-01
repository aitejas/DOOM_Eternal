@echo off
REM Build script for web deployment using pygbag (Windows)

echo Building DOOM-style Game for Web...
echo This will create a web-playable version

REM Install pygbag if not already installed
pip install pygbag

REM Build the game
python -m pygbag --dir dist main.py

echo.
echo Build complete! The web version is in the 'dist' folder.
echo To test locally, run: python -m http.server in the dist folder
echo Then visit http://localhost:8000 in your browser
