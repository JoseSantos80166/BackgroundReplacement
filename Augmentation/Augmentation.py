
from turtle import width
from PIL import Image, ImageDraw, ImageFilter
import cv2


path_to_file="Annotations/2.txt"
mode='r' #read only (r)

file=open(path_to_file, mode)

a=file.readline()
b=a.split()
print(a)
print(b[1:5])
file.close()

im = cv2.imread("Images/2.jpg")
height, width, *_= im.shape

left = (float(b[1])-(float(b[3])/2))*width
top = (float(b[2])+(float(b[4])/2))*height
right = (float(b[1])+(float(b[3])/2))*width
bottom = (float(b[2])-(float(b[4])/2))*height

print("width and height")
#print(width)
#print(height)
print("Crop dimensions")
print(int(left))
print(int(top))
print(int(right))
print(int(bottom))


#im1 = im.crop(float(b[1]))
#im1=im[200:250, 100:500]
im1= im[int(bottom):int(top), int(left):int(right)]
cv2.imshow("Cropped",im1)


# Filename
filename = 'temp1.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, im1)

imtocopy = Image.open('temp1.jpg')
background = Image.open('background/wood.jpg')
widthtarget, heighttarget = background.size

print("target location")
posx=int(float(b[1])*widthtarget)
posy=int(float(b[2])*heighttarget)

print(posx)
print(posy)

background.paste(imtocopy,(posx, posy))
background.save('background/twoimages.jpg', quality=95)