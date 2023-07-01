# Sebastian_Garcia_proyectoM2.py

Este es un codigo que desarolle estando en el curso anterior de Ucamp

El código proporcionado consta de dos partes. La primera parte se encarga de solicitar al usuario que ingrese una palabra y luego 
determinar su longitud. La segunda parte solicita al usuario que ingrese las coordenadas x e y de un punto y luego determina en qué 
cuadrante se encuentra ese punto.

Aquí está el desglose paso a paso del código:


Parte 1: Deteción de Longitud de palabra
Se imprimen tres líneas vacías y una línea con una tabulación, lo cual crea un espaciado visual en la salida.
Se muestra un mensaje para indicar que se realizará la detección de la longitud de una palabra.
Se solicita al usuario que ingrese una palabra utilizando la función input(), y el valor ingresado se asigna a la variable palabra.
Se utiliza la función len() para determinar la longitud de la palabra ingresada y se guarda en la variable longitud.
Se verifica la longitud de la palabra utilizando una estructura condicional if-elif-else.

Si la longitud es mayor o igual a 4 y menor o igual a 8, se imprime el mensaje "La palabra es correcta."
Si la longitud es menor que 4, se imprime un mensaje que indica cuántas letras faltan.
En cualquier otro caso (longitud mayor a 8), se imprime un mensaje que indica cuántas letras sobran.



Parte 2: Deteción del cuadrante
Se imprimen tres líneas vacías y una línea con una tabulación, nuevamente para el espaciado visual.
Se muestra un mensaje para indicar que se realizará la detección del cuadrante de un punto.
Se solicita al usuario que ingrese las coordenadas x e y del punto utilizando las funciones float(input()), y los valores ingresados se asignan a las variables x e y respectivamente.
Se utiliza una estructura condicional if-elif-elif-else para determinar el cuadrante en el que se encuentra el punto.

Si cualquiera de las coordenadas es igual a cero, se imprime el mensaje "Las coordenadas no pueden ser cero."
Si tanto x como y son mayores que cero, se imprime el mensaje "El punto se encuentra en el primer cuadrante."
Si x es menor que cero y y es mayor que cero, se imprime el mensaje "El punto se encuentra en el segundo cuadrante."
Si tanto x como y son menores que cero, se imprime el mensaje "El punto se encuentra en el tercer cuadrante."
En cualquier otro caso (x es mayor que cero y y es menor que cero), se imprime el mensaje "El punto se encuentra en el cuarto cuadrante."



En resumen, este código realiza la detección de la longitud de una palabra ingresada por el usuario y determina en qué cuadrante 
se encuentra un punto con coordenadas x e y ingresadas por el usuario.
