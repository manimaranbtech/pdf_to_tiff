from pdf2image import convert_from_path
from PIL import Image, ImageOps

def pdf_to_tiff(input_pdf_path, output_tiff_path, dpi=200):
    """
    Convert PDF to multi-page TIFF with CCITT T.4 (Group 3) compression
    
    Args:
        input_pdf_path: Path to input PDF file
        output_tiff_path: Path for output TIFF file
        dpi: Resolution in dots per inch (default: 200)
    """
    # Convert PDF to PIL Images
    images = convert_from_path(input_pdf_path, dpi=dpi)
    
    processed_images = []
    for img in images:
        # Convert to grayscale then to 1-bit (black & white)
        bw_img = img.convert('L').convert('1')
        processed_images.append(bw_img)
    
    # Save as multi-page TIFF with CCITT T.4 compression
    if processed_images:
        processed_images[0].save(
            output_tiff_path,
            format="TIFF",
            compression="group3",  # CCITT T.4 compression
            save_all=True,
            append_images=processed_images[1:],
            dpi=(dpi, dpi)  # This was the missing closing parenthesis
        )  # This closes the save() method call
        print(f"Successfully converted {len(processed_images)} pages to {output_tiff_path}")
    else:
        print("Error: No pages were converted")

# Example usage
pdf_to_tiff(
    input_pdf_path="example.pdf",
    output_tiff_path="output.tiff",
    dpi=200
)
