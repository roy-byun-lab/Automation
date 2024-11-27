"""Extract All Images from a PDF Document in Python"""
import fitz

# Load a PDF document
doc = fitz.open('test.pdf')

for page_number in range(len(doc)):
    page = doc[page_number]
    images = page.get_images(full=True) # get Images

    for img_index, img in enumerate(images):
        xref = img[0] # Loaction of Image
        base_image = doc.extract_image(xref) # convert Image to bytes
        image_bytes = base_image["image"]
        image_extension = base_image["ext"] # get Image FMT
        image_filename = f"2.py_page{page_number + 1}_img{img_index + 1}.{image_extension}"

        # save image
        with open(image_filename, "wb") as f:
            f.write(image_bytes)

        print(f"saved: {image_filename}")