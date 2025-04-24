import os
import hashlib
import shutil

FOLDER_TARGET = './content'
FOLDER_DUPLICATED_FILES = './duplicated'

os.makedirs(FOLDER_DUPLICATED_FILES, exist_ok=True)

def calculateHash(folder: str) -> str:
    hash_sha256 = hashlib.sha256()
    with open(folder, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b""):
            hash_sha256.update(bloco)
    return hash_sha256.hexdigest()

hashs = {}

for root, dirs, files in os.walk(FOLDER_TARGET):
    index = 1
    for file in files:
        index = index + 1
        if(index % 1000 == 0):
          print(file)

        fullPath = os.path.join(root, file)
        hasFile = calculateHash(fullPath)

        if hasFile in hashs:
            print(f'Duplicated File: {fullPath}')
            dest = os.path.join(FOLDER_DUPLICATED_FILES, os.path.basename(fullPath))
            
            counter = 1
            while os.path.exists(dest):
                base, ext = os.path.splitext(os.path.basename(fullPath))
                dest = os.path.join(FOLDER_DUPLICATED_FILES, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(fullPath, dest)
        else:
            hashs[hasFile] = fullPath
