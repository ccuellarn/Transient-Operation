import Operations as mod
import pandas as pd

def ejecutar_cargar_datos() -> pd.DataFrame:
    ruta = input("Ingrese Latitud del observador: ")
    resultados = mod.cargar_datos(ruta)
    print("Latitud encontrada")
    return resultados

    
def mostrar_menu() -> None:
    print("\nMenú de opciones:")
    print("1. Cargar datos Dec")
    print("2. Salir")


def iniciar_aplicacion() -> None:
    continuar = True

    while continuar:
        mostrar_menu()

        opcion = int(input("Ingrese la opción que desea ejecutar: "))
        if opcion == 1:
            datos = ejecutar_cargar_datos()
        elif opcion == 2:
            continuar = False
        else:
            print(
                "Ingresó una opción no válida, por favor elija una de las opciones del menú")


iniciar_aplicacion()