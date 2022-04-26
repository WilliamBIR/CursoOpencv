# Uso
# python bitwise.py

# importar paquetes
import numpy as np
import cv2

# dibujar un rectangulo
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# dibujar un circulo
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# a bitwise 'AND' is only 'True' when both inputs have a value that
# is "ON' -- in this case, the cv2.bitwise_and function examines
# every pixel in the rectangle and circle; if *BOTH* pixels have a
# value greater than zero then the pixel is turned 'ON (i.e., 255)
# in the output image; otherwise, the output value is set to
# 'OFF' (i.e., 0)


#Un bitxbit (bitwise) 'and' se vuelve 'True' cuando ambos valores
#tienen un valor que puede ser considerado 'On'.
#En este caso, se examina el circulo junto al rectangulo, y si el valor es mayor a zero,
#el pixel es considerado 'on'
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)


#Para el bitwise 'Or', se toman en cuentas los bits de ambos igualmente,
#pero en este caso, si cualquiera de los 2 son mayores a 0,e valor es 255, sino 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# the bitwise 'XOR' is identical to the 'OR' function, with one
# exception: both the rectangle and circle are not allowed to *BOTH*
# have values greater than 0 (only one can be 0)

#el bitwise 'Xor' es identico a la funcion 'Or', pero si ambos tienen mayores
#valores a 0, el valor final es 0
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# El bitwise Not, invierte los valores, 0 a 255 y 255 a 0
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)