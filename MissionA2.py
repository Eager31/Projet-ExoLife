import cv2

#Récupération de l'image
img = cv2.imread('Images/Mars_surface.pbm')

isize = img.shape  #Propriétés de l'images
vPixMax = 0
vPix = 0
compteur = 0
tauxHumidité = 0
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        vPix = vPix + img[i][j]
        compteur = compteur +1
    
vPixMax = compteur *255
##Principe de la densité : M / V ==> Moyenne
tauxHumidité = vPix / vPixMax
print("TauxHumidité :", tauxHumidité)
cv2.imshow('Surface de Mars',img)
cv2.waitKey(0)
cv2.destroyAllWindows()