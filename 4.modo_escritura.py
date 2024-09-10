
def leer_documento(nombre_archivo):
    archivo  = open(nombre_archivo, "r+")
    contenido = archivo.read()
    archivo.close()
    return contenido

def editar_documento(nombre_archivo, nuevo_contenido):
    archivo  = open(nombre_archivo, "w")
    archivo.write(nuevo_contenido)
    archivo.close()
    return f"Nuevo contenido:\n{nuevo_contenido}"


def main():
    contenido = leer_documento("datos.html")
    print(f"Contenido original:\n {contenido}")
    contenido = contenido.replace("h1", "h2")
    respuesta = editar_documento("datos.html", contenido)
    print(respuesta)
    
main()