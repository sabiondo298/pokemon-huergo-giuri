#-----------------Imports-----------------------#

import os
import json
from hash_table import cargar_pokemon_data, crear_pokemon_hash_table
from ver_medallas import hash_set, cargar_medallas
from pc import Pc
from clase_equipo import Equipo

#----------------Nombramientos de variables--------------#

pokemon_data = cargar_pokemon_data('pokemon_data.json')
pokemon_table = crear_pokemon_hash_table(pokemon_data)
medallas_data = cargar_medallas('medallas.json')
medallas = hash_set()
equipo_jugador = Equipo(6)



    
#------------------Juego principal-----------------------#

def game():
    while True:
        try:
            os.system("cls")
            opcion = int(input("ingrese la opcion que desea hacer: \n 1. Buscar un pokemon por ID \n 2. Ver Equipo \n 3. Ver Medallas \n 4. Salirse \n Opcion: "))

#------------------Busqueda por id de pokemones-----------------#

            if opcion == 1:
                os.system("cls")
                pokemon_id = int(input("Ingrese el ID del Pokémon que desea buscar: "))
                pokemon = pokemon_table.get(pokemon_id)
                if pokemon:
                    print(f"Pokémon encontrado: {pokemon}")
                else:
                    print("Pokémon no encontrado.")
                input("Presiona Enter para continuar...: ")

#------------------Ver equipo-----------------#

            elif opcion == 2:
                os.system("cls")
                equipo_jugador.display()
                input("Presione enter para continuar... ")


#------------------Ver medallas-----------------#

            elif opcion == 3:
                os.system("cls")
                medallas.add(medallas_data[0]) #prueba
                
                print("Medallas obtenidas:")
                medallas.mostrar()
                input("Presiona Enter para continuar...: ")

#------------------Salirse del juego-----------------#

            elif opcion == 4:
                os.system("cls")
                print("Saliendo del juego...")
                break
        except ValueError:
            os.system("cls")
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presiona Enter para continuar...: ")



while True:

    try:
        os.system("cls")
        print("Bienvenido al juego de Pokémon")
        print("1. Jugar")
        print("2. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            try:
                os.system("cls")
                inicial_elegido = int(input("Elige tu inicial \n 1. Bulbasaur \n 2. Charmander \n 3. Squirtle \n Eleccion: "))
                if inicial_elegido == 1:
                    pokemon_inicial = pokemon_table.get(1)
                elif inicial_elegido == 2:
                    pokemon_inicial = pokemon_table.get(4)
                elif inicial_elegido == 3:
                    pokemon_inicial = pokemon_table.get(7)
                else:
                    pokemon_inicial = pokemon_table.get(1)
                    print("Opción no válida. Se usará Bulbasaur por defecto.")

                if pokemon_inicial:
                    equipo_jugador.add(pokemon_inicial)
                    print(f"Has elegido a {pokemon_inicial.nombre} como tu inicial.")
                    input("Presiona Enter para continuar...:")
            except ValueError:
                print("Entrada no válida. Se usará Bulbasaur por defecto.")
                pokemon_inicial = pokemon_table.get(1)
                if pokemon_inicial:
                    equipo_jugador.add(pokemon_inicial)
                    input("Presiona Enter para continuar...:")

            game()
            break
        elif opcion == 2:
            print("Saliendo del juego...")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
    except ValueError:
        os.system("cls")
        print("Entrada no válida. Por favor, ingrese un número.")


    
