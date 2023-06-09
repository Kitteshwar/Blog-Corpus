import os
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def remove_paragraph(directory_path, paragraph):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encoding = detect_encoding(file_path)
            with open(file_path, 'r',encoding=encoding) as f:
                content = f.read()
            # replace the paragraph with nothing
            content = content.replace(paragraph, '')
            with open(file_path, 'w',encoding=encoding) as f:
                f.write(content)

# Path to the directory where the files are
directory_path = 'F:/fisdomGPT'
# The paragraph to remove
paragraph = """"""

remove_paragraph(directory_path, paragraph)