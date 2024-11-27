"""Extract Images from a Specific Page in Python"""
import fitz

# Load a PDF document
doc = fitz.open('test.pdf')

page = doc[0]
images = page.get_images(full=True)

for img_index, img in enumerate(images):
    xref = img[0] # Loaction of Image
    
    base_image = doc.extract_image(xref) # convert Image to bytes
    image_bytes = base_image["image"]
    image_extension = base_image["ext"] # get Image FMT
    image_filename = f"1.py_page{1}_img{img_index + 1}.{image_extension}"

    # save Image
    with open(image_filename, "wb") as f:
        f.write(image_bytes)
    print(f"saved: {image_filename}")

doc.Close()