# USAGE
# python aritmetica.py

# importar paqueteria
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="grand_canyon.png",
	help="path to the input image")
args = vars(ap.parse_args())



#Las imagenes en Numpy son guardadas como enteros de 8 bits sin signo,
#Es decir, en un rango de 0 a 255, asi que las sumas y restas entraran
#en este rando despues de aplicar la operacion.
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))


#si no se usa numpy, el resultado dara la vuelta ya sea hacia 256 o 0
added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))

# Cargar imagen original y mostrar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#incrementar la intensidad de los pixeles x100
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

# quitar 50 de todos los pixeles para disminuir intensidad
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)