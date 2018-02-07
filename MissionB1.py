import numpy as np
import cv2

cv2.destroyAllWindows()

#Récupération de l'image
img = cv2.imread('Images/Gliese 667Cc_surface.pbm',0)

a = np.double(img)
b = a + 100 ##Augmente la luminosité de l'image
img2 = np.uint8(b)


cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
