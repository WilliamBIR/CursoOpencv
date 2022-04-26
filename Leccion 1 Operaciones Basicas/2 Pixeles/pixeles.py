# Para usar
# python pixeles.py

# importar paquetes
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to the input image")
args = vars(ap.parse_args())

#Cargar imagen original y mostrar
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

#El inicio de la imagen, marcado por 0,0; se encuentra en la esquina superior
#izquierda de la imagen
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# pixel ubicado en  x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# cambiar el color del pixel (50, 20) a rojo
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#El centro de la imagen esta ubicado en
(cX, cY) = (w // 2, h // 2)

#Debido a las propiedades de numpy, es posible cortar la imagen
#de acuerdo a los valores de los pixeles.
#En este caso se muestra la esquina superio izquierda
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

#Cortando las demas esquinas por:
#1. esquina superior derecha
#2. esquina inferior derecha
#2. esquina inferior izquierda
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# Es posible cambiar un rango de pixeles a un color determinado.
image[0:cY, 0:cX] = (0, 255, 0)

# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)