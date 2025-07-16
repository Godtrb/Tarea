from tokenize import Double

estudiantes={}
cantidad=int(input(f"\nIngrese la cantidad de estudiantes: "))
for i in range(cantidad):
    print(f"\n producto #{i+1}:")
    codigo=input("Ingrese el codigo del producto: ")
    if codigo>0:
        if codigo not in estudiantes:

                nombre=input("Ingrese el nombre del producto: ")
                precio=float(input("Ingrese el precio: "))

                if (precio>0):
                    categoria = input("Ingrese la categoria del producto: ")
                    talla = input("Ingrese la talla del producto: ")
                    cantidad = int(input("Ingrese la cantidad que se agregara del producto: "))
                    if cantidad>0:
                        estudiantes[codigo] = {
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




print("\nListe de estudiantes")
for carnet,datos in estudiantes.items():
    print(f"Carnet: {carnet}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Edad: {datos["edad"]}")
    print(f"Carrera: {datos["carrera"]}")

print(" Buscar estudiante")
ado=input("Ingrese el carnet: ")
if ado in estudiantes:
    print(f"Nombre: {estudiantes[ado]['nombre']}")
    print(f"Edad: {estudiantes[ado]['edad']}")
    print(f"Carrera: {estudiantes[ado]['carrera']}")
else:
    print("El estudiante no existe")