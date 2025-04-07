from agregar_producto import agregar_producto
from eliminar_producto import eliminar_producto
from listar_productos import listar_productos
from buscar_producto import buscar_producto
from actualizar_producto import actualizar_producto
from menu import menu
from estadodelproducto import estado
from ventadeproductos import vender_productos
#programa principal
while True:
  menu()

  accion= int(input("Que accion deseas realizar?\n"))
  if accion==1:
   agregar_producto()
  if accion==2:
    buscar_producto()
  if accion==3:
    eliminar_producto()
  if accion==4:
    actualizar_producto()
  if accion==5:
    listar_productos()
  if accion==6:
    estado()
  if accion ==7:
    vender_productos()
  
  if accion ==8:
    print("saliendo del programa...")
    break
  if accion<0 or accion>8:
    print("opcion invalida, intenta nuevamente")
    
     



