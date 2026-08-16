from agregar_producto import inventario
def actualizar_producto():
 while True:
  if len(inventario)==0:
    print("no hay productos en el inventario, por favor agregue un producto primero")
    return
  nombrebusqueda=(input("ingrese el nombre  del producto a actualizar:"))
  for producto in inventario:
   if producto["NOMBRE"]== nombrebusqueda:
      print("NOMBRE ACTUAL:",producto["NOMBRE"])
      print("CANTIDAD ACTUAL:",producto["CANTIDAD"])
      nuevonombre=(input("ingrese el nuevo nombre: "))
      producto["NOMBRE"] = nuevonombre
      nuevacantidad=int(input("ingrese la nueva cantidad:"))
      producto["CANTIDAD"]=nuevacantidad
      print("producto actualizado con exito")
      return
  
  print("producto no encontrado intente de nuevo")

if __name__== "__main__":
 actualizar_producto()