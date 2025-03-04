from pdf2image import convert_from_path
from PIL import Image, ImageOps

# Path to the PDF file
input_path = "example.pdf"

# Convert PDF to a list of PIL images
images = convert_from_path(input_path, dpi=300)
bw_image = images[0].convert('1')
inverted_image = ImageOps.invert(bw_image.convert('L')).convert('1')

# Save all pages as a multi-page TIFF
tiff_path = "output.tiff"
inverted_image.save(tiff_path, format='TIFF', dpi=(300, 300), compression='tiff_ccitt')
print(f"Saved multi-page TIFF as {tiff_path}")
