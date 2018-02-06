import numpy as np
import cv2

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/Europa_surface.pbm',0)
isize = img.shape  #Propriétés de l'images
cv2.imshow('image2',img)
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if img[i][j] > 230 :
            img[i][j] = 0
        else:
            img[i][j] = 255
cv2.imshow('image',img)
cv2.waitKey(0)