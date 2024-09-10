import os

dirname = os.path.dirname(os.path.abspath(__file__))
elementos = os.listdir(dirname)

def editar_documento(nombre_archivo, contenido):
    
    if nombre_archivo in elementos:
        opcion = input(
"""El archivo ya existe, deseas reemplazar el contenido?:
[s] -> para reemplazar
[c] -> para crear una copia
[cualquier tecla] -> para no hacer nada
Ingresa la opción: """)
        
        if opcion.lower() == "s":
            archivo  = open(nombre_archivo, "w")
            archivo.write(contenido)
            archivo.close()
            print("Archivo modificado.")
        elif opcion.lower() == "c":
            nombre_archivo = "copy_"+nombre_archivo
            archivo  = open(nombre_archivo, "w")
            archivo.write(contenido)
            archivo.close()
            print(f"Se ha creado una copia del archivo con el nombre: {nombre_archivo}")
        else:
            print("El archivo no fue modificado.")


editar_documento("datos.py", "print('nuevos datos')")