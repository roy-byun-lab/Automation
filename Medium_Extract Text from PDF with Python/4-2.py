"""Extract Tables from a Page in a PDF Document"""
# pip install pdfplumber
import pdfplumber

# Open PDF
with pdfplumber.open("test2.pdf") as pdf:
    # get page1
    page = pdf.pages[0]
    # get table
    table = page.extract_table()
    if table:
        builder = []
        for row in table:
            builder.append(" ".join(row) + "\n")
        
        # save
        with open("4-2.py_output-Tables.txt", "w", encoding="utf-8") as file:
            file.write("".join(builder))
    else:
        print("No table found on this page.")
