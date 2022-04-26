# Para usar
# python enimagen.py

# importat paquetes necesarios
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to the input image")
args = vars(ap.parse_args())

# leer imagen desde el disco
image = cv2.imread(args["image"])

# Dibujar circulo en la cara, a la altura de los ojos
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
#Rectangulo a la altura de la boca
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

#Mostrar salida
cv2.imshow("Output", image)
cv2.waitKey(0)