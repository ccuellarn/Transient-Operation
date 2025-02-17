import Operations as mod
import pandas as pd

def Observations_mod() -> pd.DataFrame:
    longitude = input("Longitude for observer in 'DD-MM-SS-(N,S,W,E)' format: ")
    latitude = input("Latitude for observer in 'DD-MM-SS-(N,S,W,E)' format: ")
    RA = input("List of right ascension in 'hmsdms' format: ")
    DEC = input("List of declination in 'hmsdms' format: ")
    Date = input("Date of today in the format 'YYYY-MM-DD HH:MM:SS' ")

    resultados = mod.Observations(longitude, latitude, RA, DEC, Date)
    print("Latitud encontrada")
    return resultados

    
def show_menu() -> None:
    print("\nOptions:")
    print("1. Determine if its observable")
    print("2. Shut off")


def iniciate_app() -> None:
    go = True

    while go:
        show_menu()

        option = int(input("Number of option: "))
        if option == 1:
            Observations_mod()
        elif option == 2:
            go = False
        else:
            print(
                "Choose, you or you crew...")


iniciate_app()