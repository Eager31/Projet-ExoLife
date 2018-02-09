import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/Gliese 667Cc_surface.pbm',0)
isize = img.shape
#plt.hist(img.ravel(),256,[0,256]); plt.show()

#Si on désire augmenter la luminosité de l'image
'''
a = np.double(img)
b = a + 100 ##Augmente la luminosité de l'image
img2 = np.uint8(b)
cv2.imshow('Gliese-STD',img2)
'''

#Mettre en noir et blanc
'''
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        #print(img2)
        if img2[i][j] > 105 :
           img2 [i][j] = 255
'''

#Normalisation
cv2.normalize(img, img, 255, 255, 1)

cv2.imshow('Normalisation',img)

#Egalisation
equ = cv2.equalizeHist(img)
cv2.imshow('Egalisation',equ)

plt.hist(img.ravel(),256,[0,256], label = "Normalisation");
plt.hist(equ.ravel(),256,[0,256], label = "Egalisation");
plt.legend(loc = "upper right")
plt.show()

##Si on souhaite enregistrer les résultats en une seule image
#res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imwrite('résultatMB1.png', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
