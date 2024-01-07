# Convert multiples ts files to mp4 using treads

import os
import subprocess
import threading
import random
import psutil
from time import sleep

# FOLDER CONFIG
input_ts_files_folder = "./input"
output_mp4_files_folder = "./output"
ts_files_converted = "./done"

# TREAD_CONFIG
QUANTITY_TREADS = 20
MAX_CPU_PERCENT = 90
MAX_MEMORY_PERCENT = 90
TIME_TO_WAIT_FREE_RESOURCES_IN_S = 2

global global_ts_files_available

global_ts_files_available = []

def convert_ts_to_mp4_and_move_to_done(ts_file: str):
    ts_file_path = os.path.join(input_ts_files_folder, ts_file)
    mp4_file = ts_file.replace('.ts', '.mp4')
    mp4_file_path = os.path.join(output_mp4_files_folder, mp4_file)

    command = ["ffmpeg", "-i", ts_file_path, "-c", "copy", mp4_file_path]

    try:
        subprocess.run(command, check=True)
        os.rename(ts_file_path, os.path.join(ts_files_converted, ts_file))
        return True
    except subprocess.CalledProcessError:
        return False


def thread_worker():
    global global_ts_files_available

    while True:
        if psutil.cpu_percent() > MAX_CPU_PERCENT or psutil.virtual_memory().percent > MAX_MEMORY_PERCENT:
            sleep(TIME_TO_WAIT_FREE_RESOURCES_IN_S)
            continue

        with threading.Lock(): # BLOCK, ALLOW ONE THREAD AT A TIME
            if not global_ts_files_available:
                break
            ts_file = random.choice(global_ts_files_available)
            global_ts_files_available.remove(ts_file)

        convert_ts_to_mp4_and_move_to_done(ts_file)


def main():
    for dir in [output_mp4_files_folder, ts_files_converted]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    global global_ts_files_available
    
    global_ts_files_available = [f for f in os.listdir(input_ts_files_folder) if f.endswith('.ts')]

    threads = []
    for _ in range(QUANTITY_TREADS):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
