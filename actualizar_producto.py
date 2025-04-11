from agregar_producto import inventario
def actualizar_producto():
 while True:
  nombrebusqueda=(input("ingrese el nombre del producto a actualizar:"))
  for producto in inventario:
   if producto["NOMBRE"]== nombrebusqueda:
      print("NOMBRE ACTUAL:",producto["NOMBRE"])
      print("CANTIDAD ACTUAL:",producto["CANTIDAD"])
      print("CATEGORIA ACTUAL:",producto["CATEGORIA"])
      nuevonombre=(input("ingrese el nuevo nombre: "))
      producto["NOMBRE"] = nuevonombre
      nuevacantidad=int(input("ingrese la nueva cantidad:"))
      producto["CANTIDAD"]=nuevacantidad
      nuevacategoria=(input("ingrese la nueva categoria"))
      producto["CATEGORIA"]= nuevacategoria
      print("producto actualizado con exito")
      return
  
  print("producto no encontrado intente de nuevo")

if __name__== "__main__":
 actualizar_producto()