import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images/Jupiter1.pbm',0)
img2 = cv2.imread('Images/Jupiter2.pbm',0)

cv2.imshow('Jupiter',img)

##Version 1 - Blending - Addition de matrices
##Nécessite matrice même taille
imgF = img.copy()
imgF = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
cv2.imshow('Blending',imgF)

###Version 2 - Blending + Oppening + Closing
isize = img.shape
isize2 = img2.shape
imgV2 = img.copy()
#On privilégie le noir avec le min
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        p1 = img[i][j]
        p2 = img2[i][j]
        imgV2[i][j] = min(p1,p2)

kernel = np.ones((2,2),np.uint8) #Kernel -> On va de deux en deux
opening = cv2.morphologyEx(imgV2, cv2.MORPH_OPEN, kernel) #On modifie ce qui est à l'exéterieur de l'image
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #On modifie ce qui est à l'intérieur de l'image

plt.hist(img.ravel(),256,[0,256],label="std",alpha = 0.5)
plt.hist(closing.ravel(),256,[0,256],label="Closing",alpha = 0.5)

cv2.imshow('Opening & Closing',closing)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()