

import pyttsx3,PyPDF2

import shutil
import os
    
source_dir = '/path/to/source_folder'
target_dir = '/path/to/dest_folder'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()