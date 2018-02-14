import cv2
from matplotlib import pyplot as plt

#Récupération de l'image
img = cv2.imread('Images/GD61.pbm',0)

#Normalisation
img2 = img.copy()
cv2.normalize(img2, img2, 255, 255, 1)

cv2.imshow('Normalisation',img2)

plt.hist(img.ravel(),256,[0,256], label = "STD");
plt.hist(img2.ravel(),256,[0,256], label = "Normalisation");
plt.legend(loc = "upper right")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
