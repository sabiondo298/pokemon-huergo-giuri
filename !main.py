#-----------------Imports-----------------------#

import os
import json
from hash_table import cargar_pokemon_data, crear_pokemon_hash_table
from ver_medallas import hash_set, cargar_medallas
from clase_pc import PC
from clase_equipo import Equipo
from clase_CentroPokemon import CentroPokemon

#----------------Nombramientos de variables--------------#

pokemon_data = cargar_pokemon_data('pokemon_data.json')
pokemon_table = crear_pokemon_hash_table(pokemon_data)
medallas_data = cargar_medallas('medallas.json')
medallas = hash_set()
equipo_jugador = Equipo(6)
centropokemon = CentroPokemon(None)
pc_jugador = PC(None)
pc_oak = []


 
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
                poder_total = sum(pokemon.poder for pokemon in equipo_jugador)
                print(f"Poder total del equipo: {poder_total}")
                input("Presione enter para continuar... ")

#------------------Ver PC-----------------#

            elif opcion == 3:
                os.system("cls")
                pc_jugador.display()
                input("Presione enter para continuar... ")


#------------------Capturar pokemones-----------------#

            elif opcion == 4:
                os.system("cls")
                print("Pokemones disponibles para atrapar:\n" 
                "(Nos basamos en el poder total de tu equipo para determinar los pokemones que podes atrapar)")
                pokemon_abilitados = []
                tabla_poder = []
                for pokemon in equipo_jugador:                    
                    tabla_poder.append(pokemon.poder)
                poder_total = sum(tabla_poder)
                print(f"El poder total de tu equipo es: {poder_total}")
                for i, bucket in enumerate(pokemon_table.tabla):
                    for pokemon in bucket:
                        if pokemon[1].poder <= poder_total:                                
                            pokemon_abilitados.append(pokemon[1])
                            print(bucket)                                
                try:
                    while True:
                        eleccion_pokemon_atrapar = int(input("Ingrese el ID del Pokémon que desea atrapar: "))
                        if pokemon_table.get(eleccion_pokemon_atrapar) in pokemon_abilitados:
                            pokemon_atrapado = pokemon_table.get(eleccion_pokemon_atrapar)
                            equipo_jugador.add(pokemon_atrapado)
                            if len(equipo_jugador.pokemones) == 6:
                                pc_jugador.add_pc(pokemon_atrapado)
                                print(f"¡Has atrapado a {pokemon_atrapado.nombre}! Tu equipo está lleno, por lo que el Pokémon atrapado ha sido enviado a la PC.")
                                input("Presione Enter para continuar...: ")
                                break
                            else:
                                print(f"¡Has atrapado a {pokemon_atrapado.nombre}!")
                                input("Presione Enter para continuar...: ")
                                break
                        elif eleccion_pokemon_atrapar not in pokemon_abilitados:
                            print("El Pokémon que ingresaste no está disponible para atrapar. Por favor, elige un Pokémon de la lista.")
                            input("Presione Enter para continuar...: ")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")

#------------------Ordenar PC-----------------#
              
            elif opcion == 5:
                os.system("cls")
                try:
                    opcion_ordenar = int(input("Elige como queres ordenar tu PC: \n1. Alfabeticamente \nOpcion: "))
                    if opcion_ordenar == 1:
                        pc_jugador.ordenar_alf()
                        print("La PC fue ordenada alfabéticamente.")
                    elif opcion_ordenar == 2:
                        print("La ordenación por poder aún no está implementada.")
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
                input("Presione Enter para continuar...: ")

#------------------Centro pokemon-----------------#

            elif opcion == 7:
                os.system("cls")
                while True:
                    try:
                        centro_eleccion = int(input("Elegi el metodo de curacion: \n1. Curar todo el equipo. \nOpcion: "))
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

#------------------Transferencia oak-----------------#

            elif opcion == 8:
                os.system("cls")
                if len(equipo_jugador.pokemones) == 1:
                    print("No puedes transferir tu último Pokémon. Debes tener al menos un Pokémon en tu equipo.")
                    input("Presiona Enter para continuar...: ")
                    continue
                print("Elige un pokemon de tu pc para transferir al Profesor Oak: ")
                PC.display(self=pc_jugador)
                while True:
                    try:
                        pokemon_elegido = int(input("Ingrese el ID del numerico del pokemon que desea transferir: "))
                        pokemon_transferido = pokemon_table.get(pokemon_elegido)
                        if pokemon_transferido:
                            pc_oak.append(pokemon_transferido)
                            pc_jugador.remove_pokemon(pokemon_elegido)
                            print(f"Has transferido a {pokemon_transferido.nombre} al Profesor Oak.")
                            input("Presiona Enter para continuar...: ")
                            break
                        break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número.")

#------------------Deshacer transferencia-----------------#

            elif opcion == 9:
                os.system("cls")
                if pc_oak:
                    pokemon_devuelto = pc_oak.pop()
                    pc_jugador.add_pc(pokemon_devuelto)
                    print(f"Has devuelto a {pokemon_devuelto.nombre} del Profesor Oak a tu PC.")
                else:
                    print("No hay Pokémon para devolver del Profesor Oak.")
                input("Presiona Enter para continuar...: ")

#------------------Gimnasios-----------------#

            elif opcion == 10:
                os.system("cls")
                try:
                    while True:
                        if len(medallas.tabla) == 0:
                            print("1. Tu proximo gimnasio es de tipo roca: Brock 💎 (400 PC Recomendado" )
                            aux_gym = int(input("Desea combatir con el lider de gimnasio? \n1. Si \n2. No \nOpcion: "))
                            if aux_gym == 1:
                                tabla_poder = []
                                for pokemon in equipo_jugador:                    
                                    tabla_poder.append(pokemon.poder)
                                    poder_total = sum(tabla_poder)
                                if poder_total >= 400:
                                    print("¡Felicidades! Has derrotado a Brock y obtenido la medalla de roca.")
                                    medallas.add("Medalla Roca")
                                    input("Presiona Enter para continuar...: ")
                                    break
                                else:
                                    print("Has perdido. Tu equipo no tiene suficiente poder para derrotar a Brock.")
                                    input("Presiona Enter para continuar...: ")
                                    break
                            elif aux_gym == 2:
                                break
                
                        if len(medallas.tabla) == 1:
                            print("1. Tu proximo gimnasio es de tipo roca: Misty 💧 (650 PC Recomendado" )
                            aux_gym = int(input("Desea combatir con el lider de gimnasio? \n1. Si \n2. No \nOpcion: "))
                            if aux_gym == 1:
                                tabla_poder = []
                                for pokemon in equipo_jugador:                    
                                    tabla_poder.append(pokemon.poder)
                                    poder_total = sum(tabla_poder)
                                if poder_total >= 650:
                                    print("¡Felicidades! Has derrotado a Misty y obtenido la medalla de roca.")
                                    medallas.add("Medalla Cascada")
                                    input("Presiona Enter para continuar...: ")
                                    break
                                else:
                                    print("Has perdido. Tu equipo no tiene suficiente poder para derrotar a Misty.")
                                    input("Presiona Enter para continuar...: ")
                                    break
                            elif aux_gym == 2:
                                break

                        if len(medallas.tabla) == 2:
                            print("1. Tu proximo gimnasio es de tipo roca: Lt. Surge ⚡ (950 PC Recomendado" )
                            aux_gym = int(input("Desea combatir con el lider de gimnasio? \n1. Si \n2. No \nOpcion: "))
                            if aux_gym == 1:
                                tabla_poder = []
                                for pokemon in equipo_jugador:                    
                                    tabla_poder.append(pokemon.poder)
                                    poder_total = sum(tabla_poder)
                                if poder_total >= 950:
                                    print("¡Felicidades! Has derrotado a Lt. Surge ⚡ y obtenido la medalla de roca.")
                                    medallas.add("Medalla Trueno")
                                    input("Presiona Enter para continuar...: ")
                                    break
                                else:
                                    print("Has perdido. Tu equipo no tiene suficiente poder para derrotar a Lt. Surge.")
                                    input("Presiona Enter para continuar...: ")
                                    break
                            elif aux_gym == 2:
                                break
                
                        if len(medallas.tabla) == 3:
                            print("1. Tu proximo gimnasio es de tipo roca: Erika  (950 PC Recomendado" )
                            aux_gym = int(input("Desea combatir con el lider de gimnasio? \n1. Si \n2. No \nOpcion: "))
                            if aux_gym == 1:
                                tabla_poder = []
                                for pokemon in equipo_jugador:                    
                                    tabla_poder.append(pokemon.poder)
                                    poder_total = sum(tabla_poder)
                                if poder_total >= 950:
                                    print("¡Felicidades! Has derrotado a Erika 🌿 y obtenido la medalla de roca.")
                                    medallas.add_medalla("Medalla Arcoiris")
                                    input("Presiona Enter para continuar...: ")
                                    break
                                else:
                                    print("Has perdido. Tu equipo no tiene suficiente poder para derrotar a Erika.")
                                    input("Presiona Enter para continuar...: ")
                                    break
                            elif aux_gym == 2:
                                break

                        if len(medallas.tabla) == 4:
                            print("1. Tu proximo gimnasio es de tipo roca: Koga  (1350 PC Recomendado" )
                            aux_gym = int(input("Desea combatir con el lider de gimnasio? \n1. Si \n2. No \nOpcion: "))
                            if aux_gym == 1:
                                tabla_poder = []
                                for pokemon in equipo_jugador:                    
                                    tabla_poder.append(pokemon.poder)
                                    poder_total = sum(tabla_poder)
                                if poder_total >= 1350:
                                    print("¡Felicidades! Has derrotado a Koga ☠️ y obtenido la medalla de roca.")
                                    medallas.add("Medalla Alma")
                                    input("Presiona Enter para continuar...: ")
                                    break
                                else:
                                    print("Has perdido. Tu equipo no tiene suficiente poder para derrotar a Koga.")
                                    input("Presiona Enter para continuar...: ")
                                    break
                            elif aux_gym == 2:
                                break
                except ValueError:
                    os.system("cls")
                    print("Entrada no válida. Por favor, ingrese un número.")
                    input("Presiona Enter para continuar...: ")


                
#------------------Ver medallas-----------------#

            elif opcion == 11:
                os.system("cls")
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


#------------------Eleccion de inicial-----------------#

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


    


