"""Extract Text from a Rectangular Area"""
import fitz 

# Open PDF file
doc = fitz.open("test.pdf")

# Select Page Num
page = doc.load_page(1)

# Set Rectangular Area (x0, y0, x1, y1)
rect = fitz.Rect(0.0, 210.0, page.rect.width, 210.0 + 60.0)

# Get text
text = page.get_text("text", clip=rect)

# Save
with open('2.py_output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Close PDF
doc.close()
