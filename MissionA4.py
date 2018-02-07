import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images/Jupiter1.pbm',0)
img2 = cv2.imread('Images/Jupiter2.pbm',0)

#Texture Splatting / Blending

##Version 1 - Classique ajout

##Nécessite matrice même taille
img3 = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow('Rendu Net',img3)
cv2.waitKey(0)