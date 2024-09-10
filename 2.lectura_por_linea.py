archivo = open("archivo.txt", "r+")

lineas = archivo.readlines()

print(lineas)

for linea in lineas:
    print(linea.strip())