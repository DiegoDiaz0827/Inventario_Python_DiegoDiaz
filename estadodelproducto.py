from agregar_producto import inventario

def estado ():
    
    agotados=[]
    proximos_en_agotarse=[]

    for producto in inventario:
     if producto["CANTIDAD"] ==0:
      agotados.append(producto)
     elif producto["CANTIDAD"] <=5:
       proximos_en_agotarse.append(producto)
    
    print("AGOTADOS:")
    for a in agotados:
      print(a)
    print("PROXIMOS EN AGOTARSE:")
    for a in proximos_en_agotarse:
      print(a)