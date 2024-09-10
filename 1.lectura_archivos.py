archivo = open("archivo.txt", "r", encoding="utf-8")

contenido = archivo.read() # retorna un string con el contenido

nombre = archivo.name

print("Nombre archivo: ", nombre)

codificacion = archivo.encoding

print(codificacion)

modo = archivo.mode

print(modo)