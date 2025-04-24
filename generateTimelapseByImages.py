import cv2
import os
import glob

input_folder = "files"  # images
output_video = "result.mp4"
frame_rate = 2

image_files = sorted(glob.glob(os.path.join(input_folder, "*.jpg")))
if not image_files:
    raise FileNotFoundError("Not found images to timelapse")

first_image = cv2.imread(image_files[0])
height, width, layers = first_image.shape
size = (width, height)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video, fourcc, frame_rate, size)

for image_file in image_files:
    img = cv2.imread(image_file)
    if img.shape[:2] != (height, width):
        img = cv2.resize(img, (width, height))
    out.write(img)

out.release()
print(f"video created: {output_video}")
