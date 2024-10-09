'''En la clínica "La Fuerza" se requiere desarrollar un sistema de gestión de pacientes. El sistema
debe gestionar la información de los pacientes atendidos en el día. Para cada paciente, se
almacenará:
• Número de historia clínica (un número entero).
• Nombre del paciente (una cadena de texto).
• Edad del paciente (un número entero).
• Diagnóstico (una cadena de texto).
• Cantidad de días de internación (un número entero).
La información de todos los pacientes debe almacenarse en un array bidimensional, donde
cada fila representará un paciente, y las columnas contendrán los datos mencionados arriba.
Recordar que el array debe comenzar vacío.

Requerimientos:
Interfaz del programa:
• El sistema debe mostrar un menú interactivo para que el usuario pueda elegir
entre las diferentes opciones del sistema (cargar pacientes, buscar paciente
por Historia Clínica, determinar paciente con más/menos días de internación,
ordenar pacientes por número de historia clínica, salir del sistema, etc.).
• El menú debe estar dentro de un bucle que permita al usuario realizar
múltiples operaciones hasta que decida salir.'''


informacion_pacientes = []



'''Cargar pacientes:
• Permitir al usuario ingresar los datos de los pacientes, almacenando la
información en una lista anidada (arreglo bidimensional), como se muestra en
la imagen de arriba. La cantidad de pacientes a ingresar debe ser determinada
por el usuario.'''

def cargar_pacientes():
    n = int(input("Ingrese la cantidad de pacientes a ingresar: "))
    for _ in range(n):
        numero_historia_clinica = int(input("Ingrese el número de historia clínica: "))
        nombre_paciente = input("Nombre del paciente: ").capitalize()
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnostico: ").capitalize()
        cantidad_dias_internacion = int(input("Cantidad de dias de internacion: "))
        print(f"\n El paciente {nombre_paciente} ha sido agregado exitosamente.")
        print("-------------------------------------")
        informacion_pacientes.append([numero_historia_clinica, nombre_paciente, edad, diagnostico, cantidad_dias_internacion])
    return print("Volviendo al menú principal.. ")



'''Mostrar la lista de pacientes:
• Imprimir en pantalla todos los datos de los pacientes almacenados en el
arreglo bidimensional, mostrando cada fila como un paciente.'''

def mostrar_pacientes():
    for pacientes in informacion_pacientes:
        print(f'Número de historia clinica: {pacientes[0]}'
              f'\nNombre del paciente: {pacientes[1]}'
              f'\nEdad del paciente: {pacientes[2]}'
              f'\nDiagnostico: {pacientes[3]}'
              f'\nCantidad de dias de internacion: {pacientes[4]}\n')





'''Búsqueda de pacientes:
• Implementar una función que, dado el número de historia clínica de un
paciente, busque en la lista y muestre todos los datos de dicho paciente (o un
mensaje indicando que no se encontró al paciente).'''

def busqueda_pacientes():
    numero_historia_clinica = int(input("Ingrese el numero de Historia Clinica a buscar: "))
    for i in range(len(informacion_pacientes)):
        paciente = informacion_pacientes[i]
        if numero_historia_clinica == paciente[0]:
            return print(f'\nNúmero de historia clinica: {paciente[0]}'
                        f'\nNombre del paciente: {paciente[1]}'
                        f'\nEdad del paciente: {paciente[2]}'
                        f'\nDiagnostico: {paciente[3]}'
                        f'\nCantidad de dias de internacion: {paciente[4]}')
        
    print("No se encontró al paciente. \n Volviendo al menú..")





'''Ordenamiento de pacientes:
• Implementar una función que permita ordenar la lista de pacientes por el
número de Historia Clínica en forma ascendente. Se podrá utilizar cualquier
algoritmo de ordenamiento.'''

def ordenamiento_pacientes():
        
    for i in range(len(informacion_pacientes)):
        for j in range(len(informacion_pacientes) - i - 1):
            if informacion_pacientes[j][0] > informacion_pacientes[j + 1][0]:
                informacion_pacientes[j], informacion_pacientes[j + 1] = informacion_pacientes[j + 1], informacion_pacientes[j]
    print("Pacientes ordenado por historia clinica:")
    for producto in informacion_pacientes:
        print(f'\nNúmero de historia clinica: {producto[0]}'
            f'\nNombre del paciente: {producto[1]}'
            f'\nEdad del paciente: {producto[2]}'
            f'\nDiagnostico: {producto[3]}'
            f'\nCantidad de dias de internacion: {producto[4]}')
        print("-------------------------------------")

    return informacion_pacientes 




'''Determinar el paciente con mayor cantidad de días de internación:
• Implementar una función que calcule e imprima el paciente con más días de
internación, mostrando sus datos completos.'''

def paciente_mas_internacion():
    mas_internacion = informacion_pacientes[0]

    for dias in informacion_pacientes:
        if dias[4] > mas_internacion[4]:
            mas_internacion = dias

    return print(f"El paciente con más dias de internación es: {mas_internacion[1]} con: {mas_internacion[4]} dias."
                 f"\nNúmero de historia clinica: {mas_internacion[0]}")
        





'''Determinar el paciente con menor cantidad de días de internación:
• Implementar una función que calcule e imprima el paciente con menos días de
internación, mostrando sus datos completos'''

def paciente_menos_internacion():
    menos_internacion = informacion_pacientes[0]

    for dias in informacion_pacientes:
        if dias[4] < menos_internacion[4]:
            menos_internacion = dias

    return print(f"El paciente con menos dias de internación es: {menos_internacion[1]} con: {menos_internacion[4]} dia/s."
                 f"\nNúmero de historia clinica: {menos_internacion[0]}")





'''Cantidad de pacientes con días de internación mayor a 5 días.
• Implementar una función que recorra la lista de pacientes y cuente cuántos
pacientes tienen más de 5 días de internación.'''

def paciente_mayor_cinco_dias():
    contador = 0
    for dias in informacion_pacientes:
        if dias[4] > 5:
            contador += 1
    return print(f"Cantidad de pacientes que tienen más de 5 días de internación son: {contador}")





'''Promedio de días de internación de todos los pacientes.
• Implementar una función que calcule el promedio de días de internación de
todos los pacientes registrados.'''

def promedio_dias_internacion():
    contador = 0
    acumulador = 0 
    for i in range(len(informacion_pacientes)):
        contador += 1
        acumulador += informacion_pacientes[i][4]
    promedio = acumulador/contador
    return print(f'El promedio es: {promedio}')



def menu_principal():
    while True:

        print('\n ------------------ \n | Menú principal | \n ------------------ '
              '\n • 1. Cargar pacientes.'
              '\n • 2. Mostrar la lista de pacientes.'
              '\n • 3. Búsqueda de pacientes por número de Historia Clinica.' 
              '\n • 4. Ordenamiento de pacientes por número de Historia Clinica.'  
              '\n • 5. Mostrar paciente con más días de internación.'  
              '\n • 6. Mostrar paciente con menos días de internación.'
              '\n • 7. Cantidad de pacientes con más de 5 días de internación.'
              '\n • 8. Promedio de días de internación de todos los pacientes.'
              '\n • 9. Salir.'
              '\n ------------------------------------------')


        opciones = input(' ➱  Ingrese una opción (1, 2, 3, 4, 5, 6, 7, 8 o 9): ')
        print(" ------------------------------------------")

        match (opciones):

            case "1": 
                cargar_pacientes()
            case "2":
                mostrar_pacientes()
            case "3":
                busqueda_pacientes()
            case "4":
                ordenamiento_pacientes()
            case "5":
                paciente_mas_internacion()
            case "6":
                paciente_menos_internacion()
            case "7":
                paciente_mayor_cinco_dias()
            case "8":
                promedio_dias_internacion()
            case "9":
                print("Saliendo del sistema..")
                break
            case _:
                print("Opción invalida, ingrese nuevamente.")


menu_principal()
