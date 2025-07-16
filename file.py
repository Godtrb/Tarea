from tokenize import Double

productos={}
cantidad=int(input(f"\nIngrese la cantidad de estudiantes: "))
for i in range(cantidad):
    print(f"\n producto #{i+1}:")
    codigo=input("Ingrese el codigo del producto: ")
    if codigo>0:
        if codigo not in estudiantes:

                nombre=input("Ingrese el nombre del producto: ")
                precio=float(input("Ingrese el precio: Q"))

                if (precio>0):
                    categoria = input("Ingrese la categoria del producto: ")
                    talla = input("Ingrese la talla del producto: ")
                    cantidad = int(input("Ingrese la cantidad que se agregara del producto: "))
                    if cantidad>0:
                        productos[codigo] = {
                            "nombre": nombre,
                            "precio": precio,
                            "categoria": categoria,
                            "talla": talla,
                            "cantidad": cantidad
                        }
                    elif cantidad<=0:
                        print("Cantidad invalida")
                        i=i-1
                elif precio<=0:
                    print("Precio invalido.")
                    i=i-1

        else:
                print("Ya un producto con ese codigo.")
                i=i-1
    elif codigo<=0:
        print("Codigo no valido.")
        i=i-1




print("\nListe de productos")
for Codigo in productos.items():
    print(f"Codigo: {Codigo}")
    print(f"Nombre: {Codigo["nombre"]}")
    print(f"Precio: {Codigo["precio"]}")
    print(f"Categoria: {Codigo["categoria"]}")
    print(f"Talla: {Codigo["talla"]}")
    print(f"En existencia: {Codigo["cantidad"]}")

print(" Buscar producto")
ado=input("Ingrese el codigo del producto a buscar: ")
if ado in productos:
    print(f"Codigo: {ado}")
    print(f"Nombre: {ado["nombre"]}")
    print(f"Precio: {ado["precio"]}")
    print(f"Categoria: {ado["categoria"]}")
    print(f"Talla: {ado["talla"]}")
    print(f"En existencia: {ado["cantidad"]}")
else:
    print("El producto no existe")
ValorInventario=0
for Codigo in productos.items():
