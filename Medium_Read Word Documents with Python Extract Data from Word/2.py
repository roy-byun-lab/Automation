"""
Extract Text from an Entire Word Document in Python
"""
from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input.docx")

# Get text from the entire document
text = doc.GetText()

# Print result
print(text)