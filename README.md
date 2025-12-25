# unblurrit
Python tool for deblurring and enhancing photos using OpenCV. Supports multiple methods including Unsharp Masking, CLAHE, and Wiener Deconvolution for motion blur.

🔍 Unsharp Masking - Professionelle Schärfungstechnik
✨ CLAHE Detail Enhancement 
🎯 Wiener Deconvolution
📁 Batch Processing 

# Repository
git clone https://github.com/libertates/unblurrit.git
cd unblurrit

# Virtual Environment
python3 -m venv .venv
source .venv/bin/activate  # macOS

## Installation
pip install opencv-python numpy

## Application (bash)
# Single Image
python deblur.py mein_foto.jpg

## Directory Folder
python deblur.py images/

## Mixed-Methods/Triangulation
python deblur.py iamge1.jpg -m unsharp
python deblur.py iamge1.jpg -m combined

# basic - Quick sharpening
# unsharp - Unsharp masking 
# wiener - For motion blur
# enhance - Detail enhancement
# combined - Combines multiple methods
