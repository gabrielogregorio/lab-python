# pip install pillow
import os
from PIL import Image

INPUT_DIR = "./Certificados"
OUTPUT_DIR = "./CertificadosOtimizados"

SIZE_LIMIT = 0.25 * 1024 * 1024   # 0.25mb

WEBP_QUALITY = 80 

MAX_WIDTH = 1200

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")



def resize_proportionally(img, max_width):
    width, height = img.size

    if width <= max_width:
        return img

    ratio = max_width / float(width)
    new_width = int(round(width * ratio))
    new_height = int(round(height * ratio))

    new_width = max(1, new_width)
    new_height = max(1, new_height)

    return img.resize((new_width, new_height), Image.LANCZOS)



def optimize_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if not file.lower().endswith(SUPPORTED_EXTENSIONS):
            continue

        input_path = os.path.join(INPUT_DIR, file)
        file_size = os.path.getsize(input_path)

        if file_size > SIZE_LIMIT:
            with Image.open(input_path) as img:
                img = img.convert("RGB")

                if MAX_WIDTH is not None:
                    img = resize_proportionally(img, MAX_WIDTH)

                base_name = os.path.splitext(file)[0]
                output_path = os.path.join(OUTPUT_DIR, f"{base_name}.webp")

                img.save(
                    output_path,
                    "WEBP",
                    quality=WEBP_QUALITY,
                    method=6
                )
        else:
            print(f"Skipped: {file}")

    print("Done!")

optimize_images()