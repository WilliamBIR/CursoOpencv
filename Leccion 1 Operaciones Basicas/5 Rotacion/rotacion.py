# USAGE
# python rotacion.py

# importar paquetes
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# cargar imagen y mostrarla
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#calcular el centro de la imagen
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

#rotar la imagen 45 grados
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# rotar la imagen -90°
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# rotar la imagen usando un punto arbitrario en lugar del centro
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)

# usar mutils para rotar la imagen 180°
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

#rotar la imagen en sentido contrario a las manecillas del reloj 
#y mostrar la imagen completa
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)