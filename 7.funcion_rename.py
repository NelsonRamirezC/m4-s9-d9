import os

def renombrar_archivo(ruta_archivo_antiguo, ruta_archivo_nuevo):
    os.rename(ruta_archivo_antiguo, ruta_archivo_nuevo)
    


renombrar_archivo("./otro.txt", "./documentos/otro.html")