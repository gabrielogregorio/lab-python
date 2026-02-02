import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

RAW_DIR = "raw"
OUT_DIR = "fixed"

FFMPEG = "C:/ffmpeg/bin/ffmpeg.exe"

MAX_JOBS = 4

VIDEO_EXTS = (".avi", ".mp4", ".mov", ".mkv")

os.makedirs(OUT_DIR, exist_ok=True)

def convert(file):
    inp = os.path.join(RAW_DIR, file)
    out = os.path.join(OUT_DIR, os.path.splitext(file)[0] + ".mp4")

    print(f"▶ Convertendo: {file}")

    cmd = [
        FFMPEG, "-y",

        "-err_detect", "ignore_err",

        "-i", inp,

        # if > 1000p -> reduzir | if <= 1000 -> ok
        "-vf",
        "scale='min(1920,iw)':'min(1080,ih)':force_original_aspect_ratio=decrease",

        "-c:v", "h264_nvenc",

        "-preset", "p4",

        "-rc", "vbr",
        "-b:v", "3M",
        "-maxrate", "4M",
        "-bufsize", "8M",

        "-profile:v", "high",
        "-level", "4.0",
        "-pix_fmt", "yuv420p",

        "-c:a", "aac",
        "-b:a", "96k",
        "-ac", "2",
        "-ar", "44100",

        "-movflags", "+faststart",

        out
    ]

    subprocess.run(cmd, check=True)
    print(f"✅ Finalizado: {out}")

files = [f for f in os.listdir(RAW_DIR) if f.lower().endswith(VIDEO_EXTS)]

if not files:
    print("nenhum vídeo encontrado")
    return

with ThreadPoolExecutor(MAX_JOBS) as pool:
    pool.map(convert, files)

print("✅ Processo realizado")



