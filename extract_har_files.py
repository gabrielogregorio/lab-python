import json
import base64
import os

def extract_files_from_har(file_path, output_directory):
    index = 0
    with open(file_path, 'r', encoding="utf8") as file:
        har_data = json.load(file)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    file_count = 0
    for entry in har_data['log']['entries']:
        response = entry['response']
        content_type = response['content']['mimeType']
        print(content_type)
        if 'image' in content_type or 'video' in content_type or 'audio' in content_type or 'application/octet-stream' in content_type:
            url = entry['request']['url']
            filename = url.split("/")[-1]

            if 'image' in content_type:
                subdir = 'images'

            elif 'video' in content_type:
                subdir = 'videos'

            elif 'audio' in content_type:
                subdir = 'audios'

            elif 'application/octet-stream' in content_type:
                subdir = 'gifs'
            else:
                subdir = 'payloads'

            subdir_path = os.path.join(output_directory, subdir)
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)

            file_path = os.path.join(subdir_path, filename)

            encoding = response['content'].get('encoding')
            content = response['content'].get('text')

            if encoding == 'base64' and content is not None:
                index = index + 1
                with open('{} {}'.format( file_path[0:30], index), 'wb') as file:
                    file.write(base64.b64decode(content))
                file_count += 1

    print(f"Extracted {file_count} in {output_directory}.")

extract_files_from_har('./rockstargames.har', 'output_files')



