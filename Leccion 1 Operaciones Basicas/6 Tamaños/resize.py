# USAGE
# python resize.py

# importar paqueterias
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to the input image")
args = vars(ap.parse_args())

# Cargar imagen y mostrarlas
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#Cambiar el tamaño a 150 pixeles, pero para prevenir distorsiones,
#debemos calcular el radio del nuevo width con el viejo width

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# Cambiar el tamaño
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

#Volver a cambiar el tamaño, pero con 50 pixeles
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

#Para mayor facilidad, utilizar imutils, que hace el calculo solo
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)

#Diversas interpolaciones de ejemplos
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# Mostrar las interpolaciones
for (name, method) in methods:
	print("[INFO] {}".format(name))
	resized = imutils.resize(image, width=image.shape[1] * 3,
		inter=method)
	cv2.imshow("Method: {}".format(name), resized)
	cv2.waitKey(0)