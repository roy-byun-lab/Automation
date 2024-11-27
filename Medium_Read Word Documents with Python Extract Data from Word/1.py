"""
Extract Text from a Specific Paragraph in Python
"""
from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Load a Word document
doc.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input.docx")

# Get a specific section : Page Num
section = doc.Sections[0]

# Get a specific paragraph
paragraph = section.Paragraphs[3]

# Get text of the paragraph
str = paragraph.Text

# Print result
print(str)