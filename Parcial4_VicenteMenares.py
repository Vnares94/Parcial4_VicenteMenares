# Declaración de variables
sw = True
op = ""
compradores = {}
nombre_comprador = ""
tipo_entrada = ""
codigo_confirmacion = ""

# Definición de funciones
def comprar_entrada():
    while True: 
        nombre_comprador = input(f"Ingrese el nombre del comprador nro. {len(compradores) + 1}: ")
        if nombre_comprador in compradores:
            print("Ya existe un comprador con este nombre. Ingrese otro nombre.")
            continue
        if len(nombre_comprador) <= 3:
            print("El nombre del comprador debe contener al menos 4 caracteres.")
            continue
        break
    while True:
        tipo_entrada = input("Ingrese G si es una entrada General o V si es una entrada VIP: ").upper()
        if tipo_entrada not in ["G", "V"]:
            print("Ingrese una respuesta válida: G o V.")
            continue
        break
    while True:
        codigo_confirmacion = input("Ingrese el código de confirmación (debe tener al menos 6 caracteres, 1 letra mayúscula y 1 número, y no puede tener espacios en blanco): ")
        if validar_codigo(codigo_confirmacion) == False:
            continue
        break
    print(f"Se ha ingresado el comprador {nombre_comprador} exitosamente.\n")
    compradores[nombre_comprador] = {
        "Tipo de entrada": tipo_entrada,
        "Código de confirmación": codigo_confirmacion,
        }

def validar_codigo(codigo_confirmacion):
    if len(codigo_confirmacion) < 6:
        print("El código de confirmación debe tener al menos 6 caracteres.")
        return False
    for char in codigo_confirmacion:
        if char == " ":
            print("El código no debe contener espacios.")
            return False
    if codigo_confirmacion.isalpha():
        print("Debe ingresar al menos 1 número.")
        return False
    if codigo_confirmacion.isdigit():
        print("Debe ingresar al menos 1 letra mayúscula.")
        return False
    codigo_mayus = False
    for char in codigo_confirmacion:
        if char.isupper() == True:
            codigo_mayus = True
    if codigo_mayus == False:
        print("Debe haber al menos 1 letra mayúscula.")
        return False
    print("Código validado.")

def chequeo_compradores():
    if len(compradores) == 0:
        print("No existen compradores en la base de datos.\n")
        return True
    
def consultar_comprador():
    nombre_comprador = input(f"Ingrese el nombre del comprador que desea buscar: ")
    if nombre_comprador not in compradores:
        print("El comprador no se encuentra.\n")
        return
    print("Se ha encontrado el comprador:")
    print(f"Tipo de entrada: {compradores[nombre_comprador]["Tipo de entrada"]}, Código: {compradores[nombre_comprador]["Código de confirmación"]}\n")

def cancelar_compra():
    nombre_comprador = input(f"Ingrese el nombre del comprador cuya compra desea cancelar: ")
    if nombre_comprador not in compradores:
        print("El comprador no se encuentra.\n")
        return
    compradores.pop(nombre_comprador)
    print(f"La compra de {nombre_comprador} ha sido cancelada.\n")


# Ejecución del código
while sw: # Menú principal
    try: 
        print("---Menú---")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")

        op = input("Ingrese una opción: ")

        if op == "1": # Comprar entrada
            comprar_entrada()

        elif op == "2": # Consultar comprador
            if chequeo_compradores(): continue
            consultar_comprador()

        elif op == "3": # Cancelar compra
            if chequeo_compradores(): continue
            cancelar_compra()

        elif op == "4": # Salir
            print("Programa terminado...")
            sw = False

        else:
            print("¡Debe ingresar una opción válida!\n")

    except Exception as e:
        print(f"Error inesperado: {e}")




