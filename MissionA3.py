import cv2


img = cv2.imread('Images/Europa_surface.pbm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#On met le BG en gris
isize = gray.shape  #Propriétés de l'images

##VERSION 1 - Avec algorithme
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if gray[i][j] > 180 :
            gray[i][j] = 255
        else:
            gray[i][j] = 0
cv2.imshow('V.Algorithme',gray)


##VERSION 2 - Treshold
# On définit la plage de tresh
thresh = 180
maxValue = 255
ret, thresh = cv2.threshold(gray,thresh,maxValue,cv2.THRESH_BINARY)##On inverse les couleurs avec Binary_Inv
cv2.imshow('V.Treshold',thresh)


##VERSION 3 - Adaptative Treshold
th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 1003, 0)#On doit mettre un impair
cv2.imshow('V.Adaptative Treshold',th)


cv2.waitKey(0)
cv2.destroyAllWindows()