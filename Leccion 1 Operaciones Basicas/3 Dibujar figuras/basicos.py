# USAGE
# python basic_drawing.py

# Importar paquetes
import numpy as np
import cv2

#Iniciar una imagen con las siguientes caracteristicas;
# tamaño 300 x 300
#3 canales (r,g,b)
#debido a que son 0, el color es negro
canvas = np.zeros((300, 300, 3), dtype="uint8")

#Dibujar una linea verde desde laesquina superior izquierda a la esquina inferior
#derecha
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#Dibujar una linea roja de 3 pixeles de ancho
#de la derecha superior a la izquiera inferior
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Dibujar un rectangulo verde de 50x50 pixeles, tomando como referencia ambas esquinas
#la esquina 10,10 y la 60,60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Otro rectangulo, color rojo y de 5 pixeles de anchura de linea
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Otro rectangulo azul, rellenado en su totalidad
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Reiniciar el canvas y 
# localizando el centro del mismo
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

#Circulos incrementales de 25 pixeles el incremento
for r in range(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reiinciar canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# lDibujar 25 circulos aleatorios
for i in range(0, 25):
	#Radio aleatorios entre 5 y 200
	#color aleatorios rgb de 0 a 255

	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))

	cv2.circle(canvas, tuple(pt), radius, color, -1)

# display our masterpiece to our screen
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)