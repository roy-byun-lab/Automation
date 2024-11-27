"""Extract Text from an Entire PDF Document"""
import fitz  

# Open PDF
doc = fitz.open("test.pdf") # Input pdf file path

# get text
for i, page in enumerate(doc):
    text = page.get_text() 
    # save txt FMT
    with open(f'3-1.py_output-{i + 1}.txt', 'w', encoding='utf-8') as file:
        file.write(text)
doc.close()