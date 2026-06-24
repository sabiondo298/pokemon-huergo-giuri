import os
import json





def game():
    from estructuras_de_datos import cargar_pokemon_data, crear_pokemon_hash_table
    from estructuras_de_datos import hash_set
    from estructuras_de_datos import cargar_medallas, ver_medallas

    pokemon_data = cargar_pokemon_data('pokemon_data.json')
    pokemon_table = crear_pokemon_hash_table(pokemon_data)
    medallas_data = cargar_medallas('medallas.json')
    medallas = hash_set()
    
    

    while True:
        try:
            os.system("cls")
            opcion = int(input("ingrese la opcion que desea hacer: \n 1. Buscar un pokemon por ID \n 2. Ver Medallas \n 3. Salir del juego \n"))

#------------------Busqueda por id de pokemones-----------------#

            if opcion == 1:
                pokemon_id = int(input("Ingrese el ID del Pokémon que desea buscar: "))
                pokemon = pokemon_table.get(pokemon_id)
                if pokemon:
                    print(f"Pokémon encontrado: {pokemon}")
                else:
                    print("Pokémon no encontrado.")
                input("Presiona Enter para continuar...: ")

#------------------Ver medallas-----------------#

            elif opcion == 2:
                medallas.add(medallas_data[0]) #prueba
                
                print("Medallas obtenidas:")
                medallas.mostrar()
                input("Presiona Enter para continuar...: ")

#------------------Salirse del juego-----------------#

            elif opcion == 3:
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
            print("Iniciando el juego...")
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


    
