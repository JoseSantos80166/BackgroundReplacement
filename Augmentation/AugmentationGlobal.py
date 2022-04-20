
from turtle import width
from PIL import Image
import cv2
import glob
import os
import shutil
import random


file_list_A = glob.glob('Annotations\*.*')   # dir to the folder with Annotations

print("Annotation Number")                
print(len(file_list_A))


file_list_I = glob.glob('images\*.*')        # dir to the folder with images

print("Images Number") 
print(len(file_list_I))


file_list_B = glob.glob('Backgrounds\*.*')   # dir to the folder with Backgrounds

print("Backgrounds Number")
print(len(file_list_B))

i=0
while i<len(file_list_A):           # For each Annotation file
   print("I:")
   print(i)

   firsttime=True                   # First time replacing background for one image 

   mode='r'                         # read only (r)
   file=open(file_list_A[i], mode)  # open first annotation file
   for line in file:
      a=line                        # get first line of the annotation file
      b=a.split()
      print("LINE:")
      print(a)

      im = cv2.imread(file_list_I[i])  # open first image
      height, width, *_= im.shape      # get image height and width

      left = (float(b[1])-(float(b[3])/2))*width            # Get all dimension for the crop 
      top = (float(b[2])+(float(b[4])/2))*height
      right = (float(b[1])+(float(b[3])/2))*width
      bottom = (float(b[2])-(float(b[4])/2))*height

      #print("Crop dimensions")
      #print(int(left))
      #print(int(top))
      #print(int(right))
      #print(int(bottom))


      im1= im[int(bottom):int(top), int(left):int(right)]  # Crop the image
      #cv2.imshow("Cropped",im1)


      # Filename
      filename = "temp1_{}.jpg".format(str(i))             # Create temp file to save cropped image
      
      # Using cv2.imwrite() method
   
      cv2.imwrite(filename, im1)                           # Saving temp image

      imtocopy = Image.open(filename)                      # Open temp image file
      if firsttime==True:
         backgrounddir=file_list_B[random.randrange(0,len(file_list_B))]   # Select random background from folder to paste the cropped image on top of it
         background = Image.open(backgrounddir)
         firsttime=False
      else:
         backgrounddir="AugmentedImages/Images/image_{}.jpg".format(str(i))   # Get the background image with some cropped images already pasted on it
         background = Image.open(backgrounddir)
      widthtarget, heighttarget = background.size

      #background.show()
      #print("target location")
      posx=int(float(b[1])*widthtarget)            # position to paste the cropped image
      posy=int(float(b[2])*heighttarget)

      #print(posx)
      #print(posy)
      targetdir="AugmentedImages/Images/image_{}.jpg".format(str(i)) # dir to save the new image
      background.paste(imtocopy,(posx, posy))
      background.save(targetdir, quality=95)

      if firsttime:
         target="AugmentedImages/Annotations/image_{}.txt".format(str(i))   # dir to the annotation that was used
         shutil.copyfile(file_list_A[i], target)                            # copy to the new folder along with the new image 
      
      os.remove(filename)
   file.close()
   i=i+1