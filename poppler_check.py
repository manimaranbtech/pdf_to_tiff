import os
import subprocess
from pdf2image import convert_from_path
from PIL import Image

def check_poppler_installation(poppler_path):
    """Check if poppler utilities are available"""
    pdftoppm_path = os.path.join(poppler_path, "pdftoppm.exe")
    pdfinfo_path = os.path.join(poppler_path, "pdfinfo.exe")
    
    print(f"Checking pdftoppm.exe: {os.path.exists(pdftoppm_path)}")
    print(f"Checking pdfinfo.exe: {os.path.exists(pdfinfo_path)}")
    
    # Test pdfinfo command
    try:
        result = subprocess.run(
            [pdfinfo_path, "-v"],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(f"Poppler version: {result.stdout}")
    except Exception as e:
        print(f"Error testing pdfinfo: {e}")

# Check your poppler installation
poppler_path = r"D:\TIFF_conversion\Release-21.10.0-0\poppler-21.10.0\Library\bin"
check_poppler_installation(poppler_path)
