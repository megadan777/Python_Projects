

import pyttsx3,PyPDF2

#Copy PDF files from one folder to another
import shutil
import os

# Get the user's desktop directory
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

source_dir = os.path.join(desktop_dir, 'PDFS')
target_dir = os.path.join(desktop_dir, 'Programming', 'Python_Projects', 'PDF_Audio')

# Check if the source directory exists
if not os.path.exists(source_dir):
    print(f"Source directory '{source_dir}' not found.")
    exit()

file_names = os.listdir(source_dir)

for file_name in file_names:
    source_file_path = os.path.join(source_dir, file_name)
    target_file_path = os.path.join(target_dir, file_name)
    
    if not os.path.exists(target_file_path):
        shutil.copy(source_file_path, target_dir)
    else:
        print(f"{file_name} exists in {os.path.abspath(target_dir)}")


# This is just a print command that outputs to console that the
# file was already in director

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('The_Subsidiary_Hierarchy.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()