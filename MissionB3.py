import cv2
from matplotlib import pyplot as plt

#Récupération de l'image
img = cv2.imread('Images/HD215497.pbm') #Pour pouvoir utiliser du BGR
attendu = cv2.imread('Images/HD215497_2.jpg') #Photo avec couleurs

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##On l'utilise sur les if
isize = gray.shape
imgcolored = img.copy()
imgcoloredV2 = img.copy()
#V1 - Algorithmes
maxBlack = 64
maxB = 192
maxO = 192
maxR = 128
# B,G,R
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if gray[i][j] > maxO :
            imgcolored[i][j] = [0,255,255]

        if gray[i][j] < maxB :
            imgcolored[i][j] = [255,0,0]

        if gray[i][j] < maxR :
            imgcolored[i][j] = [0,0,255]

        if gray[i][j] < maxBlack :
            imgcolored[i][j] = [0,0,0]

#V2 - Intégrales
TotalPix = 0
histo = plt.hist(img.ravel(),256,[0,256], label = "STD");

#On calcule le nombre de Pixels sur l'histogramme
for i in histo[0][0:len(histo[0])]:
    TotalPix = TotalPix + i
print("Nombre total de pix :", TotalPix)

#On calcule les quarts grâce au total
premierQuart = TotalPix/4
deuxiemeQuart = premierQuart*2
troisiemeQuart = premierQuart*3
QuatriemeQuart = TotalPix

print("Premier Quart :", premierQuart)
print("Deuxième Quart :", deuxiemeQuart)
print("Troisieme Quart :", troisiemeQuart)
print("Quatrieme Quart :", QuatriemeQuart)

#Nous devons déterminer quel x de l'histogramme correspond à chaque quart
somme = 0
index = 0
for i in histo[0][0:len(histo[0])]:
    index = index + 1
    somme = somme + i
    if somme <= premierQuart:
        xPremierQuart = histo[1][index] #Va être la valeur de X où notre premier quart s'arrête
    if somme > premierQuart and somme <= deuxiemeQuart :
        xDeuxiemeQuart = histo[1][index]  # Va être la valeur de X où notre second quart s'arrête
    if somme > deuxiemeQuart and somme <= troisiemeQuart :
        xTroisiemeQuart = histo[1][index]  # Va être la valeur de X où notre troisième quart s'arrête
    if somme > troisiemeQuart :
        xQuatriemeQuart = histo[1][index] # Va être la valeur de X où notre quatrième quart s'arrête

print("PQ :", xPremierQuart)
print("DQ :", xDeuxiemeQuart)
print("TQ :", xTroisiemeQuart)
print("QQ :", xQuatriemeQuart)

#On parcourt chaque pixel de l'iamge
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if gray[i][j] <= xTroisiemeQuart :
            if gray[i][j] <= xDeuxiemeQuart :
                if gray[i][j] <= xPremierQuart:
                    #Noir en premier
                    imgcoloredV2[i][j] = [0,0,0]
                #2 eme quart = rouge
                else :
                    imgcoloredV2[i][j] = [0, 0, 255]
            #3 eme quart = bleu
            else :
                imgcoloredV2[i][j] = [255, 0, 0]
        #Dernier quart = orange
        else :
            imgcoloredV2[i][j] = [0, 255, 255]

cv2.imshow('R. Attendu',attendu)
cv2.imshow('Algo',imgcolored)
cv2.imshow('Integrales',imgcoloredV2)


plt.legend(loc = "upper right")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
