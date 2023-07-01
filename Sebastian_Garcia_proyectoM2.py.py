#Tarea 2.2 BootcampU

print("\n")
print("\n")
print("\t")
#espaciado 
print("\t\t Detecion de Longitud de palabra ")
palabra = input("Ingresa una palabra: ")
#recibir la palabra
longitud = len(palabra)
#Determinar su longitud 
if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")

#'''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("\n")
print("\t\t Detecion del cuadrante ")
#recibir datos
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

#determinar su ubicacion en los cuadrantes
if x == 0 or y == 0:
    print("Las coordenadas no pueden ser cero.")
elif x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante.")
else:
    print("El punto se encuentra en el cuarto cuadrante.")
