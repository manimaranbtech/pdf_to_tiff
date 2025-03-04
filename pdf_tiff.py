from pdf2image import convert_from_path
from PIL import Image

# Path to the PDF file
pdf_path = "example.pdf"

# Convert PDF to a list of PIL images
images = convert_from_path(pdf_path)

# Save all pages as a multi-page TIFF
tiff_path = "output.tiff"
images[0].save(tiff_path, save_all=True, append_images=images[1:], compression="tiff_deflate")
print(f"Saved multi-page TIFF as {tiff_path}")
