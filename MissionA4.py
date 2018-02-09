import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images/Jupiter1.pbm',0)
img2 = cv2.imread('Images/Jupiter2.pbm',0)

#Texture Splatting / Blending

##Version 1 - Classique ajout
'''
##Nécessite matrice même taille
imgF = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
'''

###Version 2 - Algo
isize = img.shape  #Propriétés de l'images
isize2 = img2.shape  #Propriétés de l'images
imgF = img
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        p1 = img[i][j]
        p2 = img2[i][j]
        imgF[i][j] = min(p1,p2)#On privilégie le noir avec le min

cv2.imshow('Rendu Net',imgF)
cv2.waitKey(0)