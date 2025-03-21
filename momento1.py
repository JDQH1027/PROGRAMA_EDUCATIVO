# Datos iniciales
usuarios = []
notas = {}

def registrar_usuario():
    print("\n--- Registrar Usuario ---")
    tipo_usuario = input("Tipo de usuario (profesor/estudiante/administrador): ").lower()
    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")
    usuarios.append({"tipo": tipo_usuario, "nombre": nombre, "contraseña": contraseña})
    print(f"Usuario '{nombre}' registrado con éxito.")

def login():
    print("\n--- Login ---")
    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            print(f"Bienvenido {nombre}.")
            return usuario
    print("Credenciales incorrectas.")
    return None

def menu_principal(usuario):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar notas (Profesor)")
        print("2. Consultar notas (Estudiante)")
        print("3. Gestionar usuarios (Administrador)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1" and usuario["tipo"] == "profesor":
            registrar_notas()
        elif opcion == "2" and usuario["tipo"] == "estudiante":
            consultar_notas(usuario["nombre"])
        elif opcion == "3" and usuario["tipo"] == "administrador":
            registrar_usuario()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida o no tiene permisos.")

def registrar_notas():
    print("\n--- Registrar Notas ---")
    estudiante = input("Nombre del estudiante: ")
    nota = input("Nota: ")
    if estudiante in notas:
        notas[estudiante].append(nota)
    else:
        notas[estudiante] = [nota]
    print(f"Nota registrada para {estudiante}.")

def consultar_notas(estudiante):
    print("\n--- Consultar Notas ---")
    if estudiante in notas:
        print(f"Notas de {estudiante}: {', '.join(notas[estudiante])}")
    else:
        print(f"No hay notas registradas para {estudiante}.")
    nota = input("Nota: ")
    if estudiante in notas:
        notas[estudiante].append(nota)
    else:
        notas[estudiante] = [nota]
    print(f"Nota registrada para {estudiante}.")

# Ejecución principal
while True:
    print("\n--- Bienvenido al Sistema ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        usuario_actual = login()
        if usuario_actual:
            menu_principal(usuario_actual)
    elif opcion == "3":
       print("salio exitosamente")
    break
else: 
       print("Opción no válida.")



#esto es un comentario para que todo el muendo lo veo


#este es mi segundo cambio

#este es mi ultimo comentario