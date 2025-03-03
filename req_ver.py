# Check Pillow version
from PIL import Image
print("Pillow version:", Image.__version__)

# Check if poppler-utils is installed (optional)
import subprocess
try:
    subprocess.run(["pdftoppm", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("poppler-utils is installed!")
except FileNotFoundError:
    print("poppler-utils is NOT installed.")
