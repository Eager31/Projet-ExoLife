import numpy as np
from matplotlib import pyplot as plt
import cv2


##Une deuxième solution pour déterminer le niveau de blur, en plus de la transformation de Fourrier
#Petite fonction qui retourne la mesure de Laplacian (Valeur numérique), càd le niveau de fréquence dans une valeur numérique
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

image = cv2.imread("Images/U1_surface.pbm")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)

# Si la valeur est inférieure à 100, l'image est considérée comme "blurr"
if fm < 100:
    text = "blurr"
else:
    text = "pas blurr"
print("L'image est", text, "avec : ", fm)

image = cv2.imread("Images/U1_surface.pbm",0)

#(opt) retirer le bruit
#image = cv2.GaussianBlur(image,(3,3),0)

#V1 - Filtre Laplacian
img_laplacian = cv2.Laplacian(image,cv2.CV_64F)

#V2 - Filtre Canny
img_canny = cv2.Canny(image,100,200)

#V3 - Filtre Laplacian
img_sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
img_sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

#V4 - Filtre Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(image, -1, kernelx)
img_prewitty = cv2.filter2D(image, -1, kernely)

#V5 - Filtre Hough (Détection)
img_houghcircle = image.copy()
img_hough = image.copy()

edges = cv2.Canny(img_hough,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200) ##On traite sur une canny
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img_hough,(x1,y1),(x2,y2),(0,0,255),2)

circles = cv2.HoughCircles(img_houghcircle,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img_houghcircle,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img_houghcircle,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("img_hough",img_hough)
cv2.imshow("img_houghcircle",img_houghcircle)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.subplot(131),plt.imshow(image, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_canny, cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(131),plt.imshow(img_sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_sobely, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_sobel, cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(131),plt.imshow(img_prewittx, cmap = 'gray')
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_prewitty, cmap = 'gray')
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_prewittx + img_prewitty, cmap = 'gray')
plt.title('Prewitt'), plt.xticks([]), plt.yticks([])
plt.show()