import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Images/Gliese 667Cc_surface.pbm',0)
isize = img.shape

#V1 - Augmenter la luminosité
imgLumino = img.copy()
a = np.double(img)
b = a + 100 ##Augmente la luminosité de l'image
imgLumino = np.uint8(b)
cv2.imshow('Lumino',imgLumino)

#V2 - Noir et blanc
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        #print(img2)
        if imgLumino[i][j] > 105 :
            imgLumino [i][j] = 255
cv2.imshow('Black & White',imgLumino)

#V3 - Normalization
img2 = img.copy()
cv2.normalize(img2, img2, 255, 255, 1)
cv2.imshow('Normalisation',img2)

#V4 - Egalisation -> Quand on fait une égalisation, ça fait une normalisation
img3 = img.copy()
equ = cv2.equalizeHist(img3)
cv2.imshow('Egalisation',equ)

plt.hist(img.ravel(),256,[0,256], label = "Standart");
plt.hist(img2.ravel(),256,[0,256], label = "Normalisation");
plt.hist(equ.ravel(),256,[0,256], label = "Egalisation");
plt.legend(loc = "upper right")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
