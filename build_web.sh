#!/bin/bash
# Build script for web deployment using pygbag

echo "Building DOOM-style Game for Web..."
echo "This will create a web-playable version"

# Install pygbag if not already installed
pip install pygbag

# Build the game
python -m pygbag --dir dist main.py

echo "Build complete! The web version is in the 'dist' folder."
echo "To test locally, run: python -m http.server in the dist folder"
echo "Then visit http://localhost:8000 in your browser"
