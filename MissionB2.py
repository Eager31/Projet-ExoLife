import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/GD61.pbm',0)
plt.hist(img.ravel(),256,[0,256], label = "STD");
#Normalisation
cv2.normalize(img, img, 255, 255, 1)

cv2.imshow('Normalisation',img)

plt.hist(img.ravel(),256,[0,256], label = "Normalisation");
plt.legend(loc = "upper right")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
