#-----------------Imports-----------------------#

import os
import json
from hash_table import cargar_pokemon_data, crear_pokemon_hash_table
from ver_medallas import hash_set, cargar_medallas
from clase_pc import Pc
from clase_equipo import Equipo
from clase_CentroPokemon import CentroPokemon

#----------------Nombramientos de variables--------------#

pokemon_data = cargar_pokemon_data('pokemon_data.json')
pokemon_table = crear_pokemon_hash_table(pokemon_data)
medallas_data = cargar_medallas('medallas.json')
medallas = hash_set()
equipo_jugador = Equipo(6)
centropokemon = CentroPokemon(None)


 
#------------------Juego principal-----------------------#

def game():
    while True:
        try:
            os.system("cls")
            opcion = int(input("Ingrese la opcion que desea hacer:\n" "1. Ver Pokédex\n""2. Ver Equipo Principal\n""3. Ver PC\n""4. Capturar nuevo Pokémon\n""5. Ordenar PC\n""6. Buscar Pokémon en Equipo\n""7. Enviar Pokémon al Centro Pokémon\n""8. Transferir Pokémon al Profesor Oak\n""9. Deshacer última transferencia\n""10. Desafiar Líder de Gimnasio\n""11. Ver Medallas\n12. Salir\nOpción: "))

#------------------Menu pokedex-----------------#

            if opcion == 1:
                os.system("cls")
                pokedex_navegacion = int(input("Elige lo que quieres hacer: \n 1. Ver pokedex completa. \n 2. Buscar por ID a un pokemon.\n 3. Salir. \n Opcion: "))
                while True:
                    try:
                        if pokedex_navegacion == 1:
                            pokemon_table.display()
                            input("Presione enter para continuar...")
                            break
                        
                        elif pokedex_navegacion == 2:    
                            pokemon_id = int(input("Ingrese el ID del Pokémon que desea buscar: "))
                            pokemon = pokemon_table.get(pokemon_id)
                            if pokemon:
                                print(f"Pokémon encontrado: {pokemon}")
                            else:
                                print("Pokémon no encontrado.")
                            input("Presiona Enter para continuar...: ")
                            break
                        
                        elif pokedex_navegacion == 3:
                            break
                    except ValueError:
                        os.system("cls")
                        print("Entrada no válida. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...: ")

#------------------Ver equipo-----------------#

            elif opcion == 2:
                os.system("cls")
                equipo_jugador.display()
                input("Presione enter para continuar... ")

#------------------Capturar pokemones-----------------#

            elif opcion == 4:
                os.system("cls")
                print("Pokemones disponibles para atrapar:\n" 
                "(Nos basamos en el poder total de tu equipo para determinar los pokemones que podes atrapar)")
                poder_total = sum(pokemon.poder for pokemon in equipo_jugador)
                print(f"Tu poder total es: {poder_total}, y los pokemones disponibles segun tu poder son:")
                for pokemon in pokemon_table.values():
                    if pokemon.poder <= poder_total:
                        print(pokemon)
                        input("Presione Enter para continuar...: ")
#------------------Centro pokemon-----------------#

            elif opcion == 7:
                os.system("cls")
                while True:
                    try:
                        centro_eleccion = int(input("Elegi el metodo de curacion: \n1. Curar todo el equipo. \n2. Curar solo uno. \nOpcion: "))
                        if centro_eleccion == 1:
                            for pokemon in equipo_jugador: # se iteran en los pokemones del usuario FIFO
                                centropokemon.curar(pokemon)
                                input("Presione Enter para continuar...: ")
                                break
                        elif centro_eleccion == 2:
                            pass
                    except ValueError:
                        os.system("cls")
                        print("Entrada no válida. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...: ")

#------------------Centro pokemon-----------------#

            elif opcion == 8:
                pass
                

#------------------Ver medallas-----------------#

            elif opcion == 11:
                os.system("cls")
                medallas.add(medallas_data[0]) #prueba
                
                print("Medallas obtenidas:")
                medallas.mostrar()
                input("Presiona Enter para continuar...: ")

#------------------Salirse del juego-----------------#

            elif opcion == 12:
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

            game() # se inicia el main game despues de elegir al inicial
            break
        elif opcion == 2:
            print("Saliendo del juego...")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
    except ValueError:
        os.system("cls")
        print("Entrada no válida. Por favor, ingrese un número.")


    
