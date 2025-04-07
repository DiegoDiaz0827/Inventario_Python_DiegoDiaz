from agregar_producto import inventario

def vender_productos():
  while True:
   nombrebusqueda=input("ingrese el nombre del producto que se VENDERA:")
   cantidadescontar=int(input("ingrese la cantidad que se vendera:"))
   for producto in inventario:
     if producto["NOMBRE"]==nombrebusqueda:
      
        producto["CANTIDAD"]-=cantidadescontar
        print("venta registrada correctamente")
        return
     else:
        print("el producto no fue encontrado")