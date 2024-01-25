

import pyttsx3,PyPDF2

#Copy PDF files from one folder to another
import glob
import shutil
import os
    
source_dir = '/Desktop/PDFS'
target_dir = '/Desktop/Programming/Python_Projects/PDF_Audio'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    if file not in glob.glob(os.path.join(target_dir, GLOB_PARMS)):
        shutil.copy(os.path.join(source_dir, file_names), target_dir)
    else:
    print("{} exists in {}".format(
        file,os.path.join(os.path.split(target_dir)[-2:])))
# This is just a print command that outputs to console that the
# file was already in director

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