import cv2

#Récupération de l'image
img = cv2.imread('Images/Encelade_surface.pbm')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
isize = gray.shape  #Propriétés de l'images
maxi = 0 #Plus c'est haut plus c'est blanc
coord = [] #Coordonnées
liste = [] #Liste qui va contenir toutes les coordonnées
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if gray[i][j] >= maxi:
            if gray[i][j] > maxi:
                liste.clear()
                maxi = gray[i][j]
                coord = [i, j]
                liste.append(coord)
            if gray[i][j] == maxi:
                liste.append(coord)


#On entoure donc la valeur la plus blanche de l'image
for i in liste :
    img = cv2.circle(img, (i[0],i[1]),10, (0,0,255), 1)

print("Coordonnées les plus blanches :",coord)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()