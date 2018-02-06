import numpy as np
import cv2

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/Encelade_surface.pbm',0)

isize = img.shape  #Propriétés de l'images
maxi = 0 #Plus c'est haut plus c'est blanc
coord = [] #Coordonnées
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if img[i][j] > maxi:
            maxi = img[i][j]
            coord = [i, j]

#On entoure donc la valeur la plus blanche de l'image
img = cv2.circle(img, (coord[0], coord[1]), 10, (255,0,0), 1)
print(coord)
cv2.imshow('image',img)
cv2.waitKey(0)

