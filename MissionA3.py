import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.destroyAllWindows()
img = cv2.imread('Images/Europa_surface.pbm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#On met le BG en gris

#Récupération de l'image
isize = gray.shape  #Propriétés de l'images

##VERSION 1 - Avec algorithme
'''
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if gray[i][j] > 180 :
            gray[i][j] = 0
        else:
            gray[i][j] = 255
cv2.imshow('Surface de Europa',gray)
'''
##VERSION 2 - Image segmentation

# On définit la plage de tresh
thresh = 180
maxValue = 255

ret, thresh = cv2.threshold(gray,thresh,maxValue,cv2.THRESH_BINARY_INV)##On inverse les couleurs avec Binary_Inv

cv2.imshow('Surface de Europa',thresh)

cv2.waitKey(0)