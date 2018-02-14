import imutils
import cv2

image = cv2.imread("Images/U2_surface.pbm")

#On passe en Canny
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 200, 300)


#On va chercher les contours sur la canny
compt = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#Eviter erreur: contours is not a numpy array, neither a scalar
compt = compt[0] if imutils.is_cv2() else compt[1]

#On sort pour pouvoir reconnaître le premier
compt = sorted(compt, key = cv2.contourArea, reverse = True)[:10] #On ne prends que les dix premiers

#Dessiner
cv2.drawContours(image, compt, 0, (0, 255, 0), 3)

cv2.imshow("Canny", canny)
cv2.imshow("Objet non identifie", image)
cv2.waitKey(0)
