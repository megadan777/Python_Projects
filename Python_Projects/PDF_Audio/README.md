# PDF to audio

The aim of this is to have the program get the PDF files from a folder on my desktop and then convert them to audio files inside this folder


import shutil
import os
    
source_dir = '/path/to/source_folder'
target_dir = '/path/to/dest_folder'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)