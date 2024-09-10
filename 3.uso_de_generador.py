def generador(archivo):
    with open(archivo, "r") as contenido:
        for linea in contenido:
            linea = linea.strip()
            yield linea
    
g1 = generador("archivo.txt")
print(type(g1))


continuar = True

try: 
    while continuar:
        print(next(g1))
        
        opcion = input("Desea seguir leyendo el documento? [s]")
        
        if opcion.lower() != "s":
            continuar = False
            
except StopIteration as e:
    print("No existen más iteraciones")
    continuar = False
    
except Exception as e:
    print("Error: ", e)
    continuar = False
    
    
print("Resto del código.")