import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/HD215497.pbm') #Pour pouvoir utiliser du BGR
img2 = cv2.imread('Images/HD215497.pbm',0) ##On l'utilise sur les if
isize = img.shape

#max = [64,64,64]
maxBlack = 64
maxB = 192
maxO = 192
maxR = 128
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if img2[i][j] > maxO :
                        #B,G,R
            img[i][j] = [0,255,255]

        if img2[i][j] < maxB :
            img[i][j] = [255,0,0]

        if img2[i][j] < maxR :
            img[i][j] = [0,0,255]

        if img2[i][j] < maxBlack :
            img[i][j] = [0,0,0]

cv2.imshow('STD',img)
plt.hist(img.ravel(),256,[0,256], label = "STD");

plt.legend(loc = "upper right")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
