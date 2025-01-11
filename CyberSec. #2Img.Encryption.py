'''
This program encrypts the image by,
manipulating pixel values and swapping the pixels.
The limitation is that it can only encrypt a photo
in jpg OR jpeg formats only.
'''
from PIL import Image
img_path = input("Enter the path of the image(.jpg OR .jpeg) only: ") # taking the path of the image {Eg.- C:\Users\saans\Downloads\sample_image.jpg}
image = Image.open(img_path)
extension = img_path.split(".") # taking the image formate 
pixel_values = image.load()

for x in range(image.width):
    for y in range(image.height):
        r, g, b = pixel_values[x, y]
        pixel_values[x, y] = (255 - r, 255 - g, 255 - b) # pixel value manipulation
        try:
            if x%2==0 and y%2==0:
                pixel_values[x,y], pixel_values[x+1, y+1]=pixel_values[x+1, y+1], pixel_values[x, y] # pixel swapping
        except IndexError:
            continue

image.save(f'encryted_image.{extension[-1]}')
