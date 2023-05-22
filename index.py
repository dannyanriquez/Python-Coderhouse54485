import json


# Función para registrar un nuevo usuario
def registrar_usuario():
    # Pedimos al usuario que ingrese sus datos
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Abrimos el archivo que contiene la base de datos de usuarios
    with open("usuarios.json", "r") as archivo:
        base_de_datos = json.load(archivo)

    # Si el usuario ya existe, le informamos al usuario y terminamos la función
    if nombre in base_de_datos:
        print("El usuario ya existe. Por favor ingrese otro nombre de usuario.")
        return

    # Si el usuario no existe, lo agregamos a la base de datos
    base_de_datos[nombre] = contrasena

    # Guardamos la base de datos actualizada en el archivo
    with open("usuarios.json", "w") as archivo:
        json.dump(base_de_datos, archivo)

    print("Usuario registrado con éxito.")




####################################################################################


# Función para mostrar la lista de usuarios registrados
def mostrar_usuarios():
    # Abrimos el archivo que contiene la base de datos de usuarios
    with open("usuarios.json", "r") as archivo:
        base_de_datos = json.load(archivo)

    print("Lista de usuarios:")
    for nombre, contrasena in base_de_datos.items():
        print(f"{nombre}: {contrasena}")
    

####################################################################################

# Función para hacer login
def hacer_login():
    # Pedimos al usuario que ingrese sus datos
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Abrimos el archivo que contiene la base de datos de usuarios
    with open("usuarios.json", "r") as archivo:
        base_de_datos = json.load(archivo)

    # Si el usuario no existe, le informamos al usuario y terminamos la función
    if nombre not in base_de_datos:
        print("El usuario no existe.")
        return

    # Si la contraseña no coincide, le informamos al usuario y terminamos la función
    if contrasena != base_de_datos[nombre]:
        print("La contraseña no es correcta.")
        return

    # Si el usuario y la contraseña son correctos, le damos la bienvenida
    print(f"Bienvenido, {nombre}!")


############################################################################

# Programa principal


while True:
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar la lista de usuarios registrados")
    print("3. Hacer login")
    print("4. Salir")

    opcion = input("Seleccione una opción: \n")

    if opcion == "1": 
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        hacer_login()
    elif opcion == "4":
        break #Si elige la opcion 4 hace un break y el loop deja de ejecutar.
    else:
        print("Opción inválida.")