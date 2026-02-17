# pip install pdf2image pillow
# https://github.com/oschwartz10612/poppler-windows/releases/tag/v25.12.0-0
# Convert PDF files to webp images


import os
from pdf2image import convert_from_path
from PIL import Image

INPUT_DIR = "./Certificados"
POPPLER_PATH = r"C:/poppler-25.12.0/Library/bin"
QUALITY = 90

def convert_pdf_to_webp(pdf_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(INPUT_DIR, f"{base_name}.webp")

    pages = convert_from_path(
        pdf_path,
        dpi=200,
        poppler_path=POPPLER_PATH
    )

    pages = [page.convert("RGB") for page in pages]

    pages[0].save(
        output_path,
        "WEBP",
        save_all=len(pages) > 1,
        append_images=pages[1:],
        quality=QUALITY,
        method=6
    )

    print(f"Save in: {output_path}\n")

def main():
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            convert_pdf_to_webp(os.path.join(INPUT_DIR, file))

if __name__ == "__main__":
    main()