"""Extract Text from a Particular Page"""
import fitz  

# Open PDF
doc = fitz.open("test.pdf") # Input pdf file path

# Get text
with open(f'1.py_output.txt', 'w', encoding='utf-8') as file:
    page = doc[0] # Set page 1
    text = page.get_text() # Get Text
    file.write(f"--- Page 1 ---\n") 
    file.write(text + "\n")
doc.close()