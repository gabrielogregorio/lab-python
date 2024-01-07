import requests
import os
import subprocess
import time
from natsort import natsorted

base_url = "...{}...ts"

#"https://vod.cf.dmcdn.net....frag(5)...ts"
#"https://vod.cf.dmcdn.net....frag(6)...ts"
#"https://vod.cf.dmcdn.net....frag(7)...ts"

output_dir = "files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

index = 1 # index ts files
while True:
    url = base_url.format(index)
    response = requests.get(url)
    
    if response.status_code == 200:
        file_name = os.path.join(output_dir, f"{index}.ts")
        with open(file_name, 'wb') as file:
            file.write(response.content)
        index += 1
    else:
        print(response.status_code)
        break

ts_files = natsorted([f for f in os.listdir(output_dir) if f.endswith(".ts")])

output_video_name = f"{int(time.time())}.mp4"
input_files = '|'.join([os.path.join(output_dir, f) for f in ts_files])
command = f"ffmpeg -i 'concat:{input_files}' -c:v libx264 -c:a aac -strict -2 {output_video_name}"
subprocess.call(command, shell=True) ## convert to mp4

for ts_file in ts_files: # drop ts files
    os.remove(os.path.join(output_dir, ts_file))

os.rmdir(output_dir) # drop output files
