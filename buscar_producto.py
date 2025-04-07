from agregar_producto import inventario
def buscar_producto():
 while True:
   nombrebusqueda=input("ingrese el nombre del producto a buscar:")
   for producto in inventario:
     if producto["NOMBRE"]==nombrebusqueda:
        print("producto encontrado")
        print(producto)
        return
   print("producto no encontrado intente de nuevo")


    
if __name__== "__main__":
 buscar_producto()