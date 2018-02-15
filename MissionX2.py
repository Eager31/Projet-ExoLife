import cv2
import numpy as np
from matplotlib import pyplot as plt

#Transformée en cosinus discrète (TCD / DCT), est une transformation proche de la DFT -> Permet réduire répétition

img = cv2.imread('Images/Gliese 581d V2.pbm')

#V1 - Fast Denoising
denoised_gray = cv2.fastNlMeansDenoising(img,None,9,13) #Pas très puissant - Nécessite couleurs
denoised_gray = np.float32(denoised_gray)/255.0
source_blur = cv2.GaussianBlur(denoised_gray, None, 3)
denoised_gray = cv2.cvtColor(denoised_gray,cv2.COLOR_BGR2GRAY)#On met le BG en gris


#On va supprimer du bruit à la main
rows, cols = denoised_gray.shape #shape retourne le nombre de lignes et de colonnes de l'image
#print(denoised_gray.shape)
#crow,ccol = int(rows/2) , int(cols/2)
#print(crow)
#print(ccol)
denoised_gray = cv2.dct(denoised_gray) #Discreet cosignus transform

#dtc[crow-200:crow-150, ccol-300:ccol-250] = 255 #It works
denoised_gray[0:30,0:30] = 0 #Forme simplifiée
cv2.imshow('Discreet Cosignus Transform',denoised_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Après les modifications, on remet par défaut
denoised_gray = cv2.dct(denoised_gray,denoised_gray,cv2.DCT_INVERSE)

#V2 - Median Blur
median = cv2.medianBlur(img,3)
median = cv2.medianBlur(median,3)

plt.subplot(131),plt.imshow(img)
plt.title('Image de base V1'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(denoised_gray, cmap = 'gray')
plt.title('Modifications DCT'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(median)
plt.title('Remove Noise via blur'), plt.xticks([]), plt.yticks([])
plt.show()
