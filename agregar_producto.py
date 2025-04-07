inventario=[]
def agregar_producto ():
  
   nombre= input("Ingrese el nombre del producto:")
   
   while True:
    cantidad= int(input("ingrese la cantidad del producto:"))
    if cantidad<0 :
     print("Numero invalido.".upper())
    else:
     print("producto registrado con exito!")
     print(f"Nombre:{nombre}\nCantidad:{cantidad}".upper())
     break
   
   estudiante={
     "NOMBRE": nombre,
     "CANTIDAD" : cantidad
     }
   inventario.append(estudiante)
   
if __name__== "__main__":
  agregar_producto()



