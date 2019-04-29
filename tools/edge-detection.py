# The following script detect edges of one single image and save it as a new image file, also show two image with plt
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('../photos/resized/pikachu.png',0)

# # detect edges
# edges = cv2.Canny(img,256,256)

# # revert white and balck
# newEdges = cv2.bitwise_not(edges)

# # save output image
# cv2.imwrite('output.png',newEdges)

# # draw result (optional)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(newEdges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

# The following script process all images in a folder, detect edges and save them as new images
import cv2
import os, os.path
import numpy as np
from matplotlib import pyplot as plt

print (cv2.__version__)
imageDir = fullfile("./photos/resized/","*.png") #specify your path here
img_dir = dir(imageDir)
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

for file in os.listdir(img_dir):
  extension = os.path.splitext(file)[1]
  if extension.lower() not in valid_image_extensions:
      continue
  image_path_list.append(os.path.join(img_dir, file))

for imagePath in image_path_list:
  print(imagePath)
  # read the img
  img = cv2.imread(imagePath,0)
  if img is None:
      continue

  # detect edges
  edges = cv2.Canny(img,50,50)

  # revert white and balck
  newEdges = cv2.bitwise_not(edges)

  # save output image in the edges folder
  path = imagePath.replace('resized', 'edges')
  cv2.imwrite(path,newEdges)
