def crear_documento_desde_lista(nombre_archivo, lista):
    archivo  = open(nombre_archivo, "w")
    archivo.writelines(lista)

    
    
def main():
    continuar = True
    clientes = []
    while continuar:
        cliente = input("Ingrese el nombre de un nuevo cliente: ")
        clientes.append(cliente+"\n")
        
        opcion = input("Desea continuar: [s] ")
        
        if opcion.lower() != "s":
            continuar = False
        
    crear_documento_desde_lista("clientes.txt", clientes)

main()