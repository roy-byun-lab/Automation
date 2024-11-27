"""Extract Images from a Word Document in Python"""
import queue
from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("C:\\Users\\Administrator\\Desktop\\input2.docx")

# Create a Queue object
nodes = queue.Queue()
nodes.put(doc)

# Create a list
images = []

while nodes.qsize() > 0:
    node = nodes.get()

    # Loop through the child objects in the doucment
    for i in range(node.ChildObjects.Count):
        child = node.ChildObjects.get_Item(i)

        # Detect if a child object is a picture
        if child.DocumentObjectType == DocumentObjectType.Picture:
            picture = child if isinstance(child, DocPicture) else None
            dataBytes = picture.ImageBytes

            # Add the image data to the list 
            images.append(dataBytes)
         
        elif isinstance(child, ICompositeObject):
            nodes.put(child if isinstance(child, ICompositeObject) else None)

# Loop through the images in the list
for i, item in enumerate(images):
    fileName = "Image-{}.png".format(i) # Image-0.png...
    with open("ExtractedImages/"+fileName,'wb') as imageFile:

        # Write the image to a specified path
        imageFile.write(item)