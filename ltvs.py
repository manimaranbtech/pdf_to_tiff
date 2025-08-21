import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_tiff(input_pdf_path, output_tiff_path, dpi=200):
    """
    Convert PDF to multi-page TIFF with CCITT T.6 (Group 4) compression
    """
    # Verify file exists
    if not os.path.exists(input_pdf_path):
        raise FileNotFoundError(f"PDF file not found: {input_pdf_path}")
    
    # Verify file is readable
    if not os.access(input_pdf_path, os.R_OK):
        raise PermissionError(f"No read permission for: {input_pdf_path}")
    
    try:
        # Convert PDF to PIL Images
        images = convert_from_path(
            input_pdf_path, 
            dpi=dpi, 
            poppler_path=r"D:\TIFF_conversion\Release-21.10.0-0\poppler-21.10.0\Library\bin"
        )
        
        processed_images = []
        for img in images:
            # Convert to grayscale then to 1-bit (black & white)
            bw_img = img.convert('L').convert('1')
            processed_images.append(bw_img)
        
        # Save as multi-page TIFF with CCITT T.6 compression
        if processed_images:
            processed_images[0].save(
                output_tiff_path,
                format="TIFF",
                compression="group4",
                save_all=True,
                append_images=processed_images[1:],
                dpi=(dpi, dpi)
            )  
            print(f"Successfully converted {len(processed_images)} pages to {output_tiff_path}")
        else:
            print("Error: No pages were converted")
            
    except Exception as e:
        print(f"Error converting PDF: {e}")
        raise

# Example usage with error handling
try:
    pdf_to_tiff(
        input_pdf_path="example1.pdf",
        output_tiff_path="output.tiff",
        dpi=200
    )
except Exception as e:
    print(f"Conversion failed: {e}")
