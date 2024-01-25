



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

import PyPDF2
import pyttsx3
import os

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the PDF file name
pdf_file_name = 'The_Subsidiary_Hierarchy.pdf'

# Combine the directory and file name to get the full path
pdf_file_path = os.path.join(script_dir, pdf_file_name)

# Open the PDF file using PdfReader
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)


# Initialize the text-to-speech engine
speaker = pyttsx3.init()

full_text = ""
for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    full_text += clean_text

#Full text print
print(full_text)

# Save the text to an MP3 file
mp3_file_path = 'The_Subsidiary_Hierarchy.mp3'
speaker.save_to_file(full_text, mp3_file_path)
speaker.runAndWait()

speaker.stop()