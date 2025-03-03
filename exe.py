from pdf2image import convert_from_path
from PIL import Image, ImageOps

pdf_path = "26267349 - BRUSH-Model.pdf"

# Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300)

    # Convert first page to black & white
    bw_image = images[0].convert('1')

    # Invert colors
    inverted_image = ImageOps.invert(bw_image.convert('L')).convert('1')

output_path = "output.tiff"

# Save as TIFF with CCITT compression
    inverted_image.save(
        output_path,
        format='TIFF',
        dpi=(300, 300),
        compression='tiff_ccitt'
    )
