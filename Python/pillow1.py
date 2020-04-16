#Here we will use python and the plugin- pillow to mess with images
from PIL.image import core as_imaging
try:
    img = Image.open(C:\Users\Administrator\Pictures\Saved Pictures\image_1)
except IOError:
    print("Unable to load image, please try again.")
    pass
img.show()
