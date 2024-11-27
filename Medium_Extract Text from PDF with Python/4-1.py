"""Extract Tables from a Page in a PDF Document"""
"""In some cases, Setting path(Ghostscript) may be necessary."""
"""No recommend"""

import camelot

# Get Table in PDF
tables = camelot.read_pdf("test2.pdf", pages='1')  # Can Set page Num

# Extraction Table Num
print(f"Number of tables extracted: {len(tables)}")

if len(tables) > 0:
    builder = []
    # Get each cells
    for table in tables:
        for row in table.data:
            for cell in row:
                builder.append(cell + " ")
            builder.append("\n")
        builder.append("\n")
    # Save
    with open("4-1.py_output-Tables.txt", "w", encoding="utf-8") as file:
        file.write("".join(builder))
else:
    print("No tables found in the PDF.")
