"""Extract Metadata of a Word Document in Python"""

from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Load a Word document
doc.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input.docx")

# Get the built-in properties of the document
builtinProperties = doc.BuiltinDocumentProperties

# Get the value of the built-in properties
properties = [
    "Author: " + builtinProperties.Author,
    "Company: " + builtinProperties.Company,
    "Title: " + builtinProperties.Title,
    "Subject: " + builtinProperties.Subject,
    "Keywords: " + builtinProperties.Keywords,
    "Category: " + builtinProperties.Category,
    "Manager: " + builtinProperties.Manager,
    "Comments: " + builtinProperties.Comments,
    "Hyperlink Base: " + builtinProperties.HyperLinkBase,
    "Word Count: " + str(builtinProperties.WordCount),
    "Page Count: " + str(builtinProperties.PageCount),
]

# Print result
for i in range(0, len(properties)):
    print(properties[i])