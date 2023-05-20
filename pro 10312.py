import os
import shutil

files = [f for f in os.listdir() if '.pdf' in f.lower()]

os.mkdir('downloaded_images')

for file in files:
    new_path = 'downloaded_images/' + files
    shutil.move(files, new_path)
