#Para correr el programa:
# python cargarimagen.py --image "jurassic_park.png"

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# Cargar la imagen desde el archivo con imread
# dimensiones de la imagen y numero de canales
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# ver el tamaño de ancho, alto y num de canales de la imagen
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# mostrar la imagen en pantalla y esperar a que se pulse una tecla.
cv2.imshow("jurassic_park", image)
cv2.waitKey(0)

# Guardar de nueva cuenta la imagen en un nuevo archivo
cv2.imwrite("newimage.jpg", image)

