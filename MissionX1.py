import numpy as np
import cv2
from matplotlib import pyplot as plt


##Ouverture depuis un .dat -> :(
'''
#_io.TextIOWrapper
test_file = open('Images/Asellus Secundus.dat', 'r', encoding='utf-8', errors='replace')
# Travailler avec les streams ==> https://docs.python.org/3/library/io.html
test_lines = test_file.readlines()
print(test_lines)
#cv2.imshow('image',test_lines)
test_file.close()
'''

#Principe de Fourier -> DFT : Discrete Fourier Transfort
''' La transformation de fourier s'exprime comme une somme infinie des fonctions tigonométriques de toutes fréquences / pulsations.
On l'utilise pour étudier des domaines de fréquence.
On passe d'un signal à un spectre grâce à sa transformation.
Exemple de fourier : https://upload.wikimedia.org/wikipedia/commons/e/e8/Periodic_identity_function.gif

Si l'amplitude varie dans un temps court, c'est un haut niveau de fréquence. 
Dans une image, plus le spectre affiche du bruit et des espacements, plus les fréquences sont hautes
'''

img = cv2.imread('Images/kamino.jpeg',0)

#FFT est un filtre passe haut, car il permet de connaître la fréquence de chaque kernel block ,et par quelle région il passe. Ainsi chaque kernel peut être passe haut ou passe bas.

#Transformation de fourier -> FFT : Fast Fourier Transform
f = np.fft.fft2(img) ##Nous donne la fréquence de transformation (array compliqué) appellé "GrayScale"
fshift = np.fft.fftshift(f) #Apporter vers le centre, en faisant N/2 sur chaque direction
spectre = 20*np.log(np.abs(fshift))
#Si on rogne des pixels
'''
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-10:crow+10, ccol-10:ccol+10] = 0
'''
#On fais la transformation inverse -> IFFT (IDFT)
f_ishift = np.fft.ifftshift(fshift) #Ramène vers en haut à gauche (et non au centre) comme à l'originelle
img_back = np.fft.ifft2(f_ishift) #On inverse le FTT
img_back = np.abs(img_back) #Conversion en float car c'est un nombre complexe

plt.subplot(141),plt.imshow(img, cmap = 'gray')
plt.title('Kamino'), plt.xticks([]), plt.yticks([])

plt.subplot(142),plt.imshow(spectre, cmap = 'gray')
plt.title('Spectre Kamino'), plt.xticks([]), plt.yticks([])

plt.subplot(143),plt.imshow(img_back, cmap = 'gray')
plt.title('Coming Back'), plt.xticks([]), plt.yticks([])

plt.subplot(144),plt.imshow(img_back) ##Si on ne met pas de gray - ringing effects (à cause de la fenêtre)
plt.title('Résultat JET'), plt.xticks([]), plt.yticks([])
plt.show()

#C'est une fonction et non une matrice, on ne peut donc pas utiliser de imgshow.
#cv2.imshow('STD',img_back)
#cv2.waitKey(0)
#cv2.destroyAllWindows()