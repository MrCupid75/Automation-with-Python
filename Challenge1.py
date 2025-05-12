import glob

def find_all_pdfs(directory):
    pdf_path_list = glob.glob(f'{directory}/**/*.pdf', recursive=True)

    return pdf_path_list

result = find_all_pdfs('C:/Users/EEK\Desktop/DRIVE D')
print(result)
"""
Your task:
Write a Python script to help lawyers find these PDF documents. The script should:

Use the glob module to search the specified directory and all its subdirectories for files with the .pdf extension and assign the result to pdf_files.

Print pdf_files to display a list of the full file paths of all the PDF documents found.

Tips:
Remember to import the glob module.

Use the recursive=True argument to search subdirectories.

Example input:
Assume the following file structure:

documents/

├── report.pdf

├── meeting_notes.txt

└── subfolder/

    └── presentation.pdf 

Expected output:
['documents\\report.pdf', 'documents\\subfolder\\presentation.pdf']
"""