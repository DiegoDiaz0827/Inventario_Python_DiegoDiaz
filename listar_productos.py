from agregar_producto import inventario
def listar_productos ():
    
     if not  inventario:
        print("no hay productos")
        return
     print("LISTA DE PRODUCTOS")
     for producto in inventario:
      print(f"NOMBRE:{producto['NOMBRE']}-CANTIDAD:{producto['CANTIDAD']}")
        
if __name__== "__main__":
  listar_productos()