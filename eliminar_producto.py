from agregar_producto import inventario

def eliminar_producto():
 while True:
  nombrebusqueda=(input("ingrese el nombre del producto a eliminar:"))
  
  for producto in inventario:
   if producto["NOMBRE"]==nombrebusqueda:
    inventario.remove(producto)
    print("producto eliminado con exito")
    return
    
  print("producto no encontrado")
     
if __name__== "__main__":
  eliminar_producto()