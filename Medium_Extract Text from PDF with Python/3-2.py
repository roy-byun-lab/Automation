"""Extract Text from an Entire PDF Document"""
import fitz  

# Open PDF
doc = fitz.open("test.pdf") # Input pdf file path

# get text
with open(f'3-2.py_output.txt', 'w', encoding='utf-8') as file:
    for page_number in range(len(doc)):
        page = doc[page_number]
        text = page.get_text()
        file.write(f"--- Page {page_number + 1} ---\n") 
        file.write(text + "\n")
doc.close()