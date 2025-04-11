inventario=[]
def agregar_producto ():
  
   nombre= input("Ingrese el nombre del producto:")
   while True:
    categoria= input("Que categoria es el producto\n(enlatados,lacteos,cereales,granos):")
    if categoria not in ["enlatados", "lácteos", "cereales", "granos"]:
     print("categoria no disponible. intente nuevamente")
    else:
     break
   while True:
      cantidad= int(input("ingrese la cantidad del producto:"))
      if cantidad<0 :
       print("Numero invalido.".upper())
      else:
       print("producto registrado con exito!")
       print(f"Nombre:{nombre}\nCantidad:{cantidad}\nCategoria:{categoria}".upper())
       estudiante={
       "NOMBRE": nombre,
       "CANTIDAD" : cantidad,
       "CATEGORIA": categoria
      }
       inventario.append(estudiante)
      break
    
   
if __name__== "__main__":
  agregar_producto()



