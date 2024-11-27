"""
Extract Tables from a Word Document in Python
"""
from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Load a Word document
doc.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input.docx")

# Iterate through the sections
for i in range(doc.Sections.Count):

    # Get a specific section
    section = doc.Sections.get_Item(i) # doc.Sections[i]

    # Get tables from the section
    tables = section.Tables

    # Iterate through the tables
    for j in range(0, tables.Count):

        # Get a certain table
        table = tables.get_Item(j)

        # Declare a variable to store the table data
        tableData = ""

        # Iterate through the rows of the table
        for m in range(0, table.Rows.Count):

            # Iterate through the cells of the row
            for n in range(0, table.Rows.get_Item(m).Cells.Count):

                # Get a cell
                cell = table.Rows.get_Item(m).Cells.get_Item(n)

                # Get the text in the cell
                cellText = ""
                for para in range(cell.Paragraphs.Count):
                    paragraphText = cell.Paragraphs.get_Item(para).Text
                    cellText += (paragraphText + "     ")

                # Add the text to the string
                tableData += cellText

            # Add a new line
            tableData += "\n"
    
        # Save the table data to a text file
        with open(f"output/WordTable_{i+1}_{j+1}.txt", "w", encoding="utf-8") as f:
            f.write(tableData)