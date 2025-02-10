import os, random, time
from clases_subclases import pokemon, mapa, personaje

almacen_Pokemons = []

with open("listado_pokemons.txt") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre, tipo, ataque, defensa = datos[0], datos[1], int(datos[2]), int(datos[3])

        match tipo:
            case 'Agua':
                pokemon_instancia = pokemon.PokemonAgua(nombre, tipo, ataque, defensa, 100)
            case 'Planta':
                pokemon_instancia = pokemon.PokemonPlanta(nombre, tipo, ataque, defensa, 100)
            case 'Fuego':
                pokemon_instancia = pokemon.PokemonFuego(nombre, tipo, ataque, defensa, 100)
            case 'Volador':
                pokemon_instancia = pokemon.PokemonVolador(nombre, tipo, ataque, defensa, 100)

        almacen_Pokemons.append(pokemon_instancia)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def informar_carga_pokemons():
    contador_tipos = {'Planta': 0, 'Agua': 0, 'Fuego': 0, 'Volador': 0}

    for p in almacen_Pokemons:
        if p.tipo in contador_tipos:
            contador_tipos[p.tipo] += 1

    print("POKEMONS CARGADOS EN EL MAPA")
    print("====================================================================================")
    for tipo, cantidad in contador_tipos.items():
        print(f"Pokémon {tipo}: {cantidad}")

    print("====================================================================================")

def cambiar_pokemon_default(nombre):
    for p in almacen_Pokemons:
        if p.nombre == nombre:
            return p

    print("Pokemon no encontrado.")
    return False

def crear_pokemon():
    nombre = input("Nombre del pokemon: ")
    tipo = input("Tipo del pokemon (Planta, Agua, Fuego, Volador): ")
    atq = int(input("ATQ: "))
    defense = int(input("DEF: "))
    ps = int(input("PS: "))

    match tipo:
        case 'Agua':
            pokemon_instancia = pokemon.PokemonAgua(nombre, tipo, atq, defense, ps)
        case 'Planta':
            pokemon_instancia = pokemon.PokemonPlanta(nombre, tipo, atq, defense, ps)
        case 'Fuego':
            pokemon_instancia = pokemon.PokemonFuego(nombre, tipo, atq, defense, ps)
        case 'Volador':
            pokemon_instancia = pokemon.PokemonVolador(nombre, tipo, atq, defense, ps)
        case _:
            print("Tipo de Pokémon no válido.")
            return

    almacen_Pokemons.append(pokemon_instancia)

# Simulación de carga
limpiar_pantalla()
print("¡Bienvenido al Simulador de Entrenador Pokémon!")
time.sleep(3)
limpiar_pantalla()
print("Cargando pokemons...")
time.sleep(0.8)
limpiar_pantalla()
print("Cargando pokemons.....")
time.sleep(1)
limpiar_pantalla()
print("Cargando pokemons........")
time.sleep(0.2)
limpiar_pantalla()
print("Cargando pokemons.............")
time.sleep(0.7)
limpiar_pantalla()
print("Cargando pokemons....................")
time.sleep(2.5)


# Loop del juego
jugador = personaje.Jugador(0, 0, 'Gabriel')
pokemon_default = almacen_Pokemons[0]

mapa_juego = mapa.Mapa(5)

menu_loop = True
while menu_loop:
    limpiar_pantalla()
    informar_carga_pokemons()
    print("1. Añadir un pokemon personalizado")
    print("2. Recargar distribución de mapa")
    print(f"3. Elegir pokemon de combate (Default: {pokemon_default.nombre})")
    print("4. Acceder al mapa")
    print("0. Salir")
    print("====================================================================================")
    accion = input("Accion => ")
    match accion:
        case '0':
            limpiar_pantalla()
            print("Cerrando juego...")
            time.sleep(1)
            menu_loop = False

        case '1':
            limpiar_pantalla()
            print("BIENVENIDO A CREAR TU POKEMON")
            print("====================================================================================")
            crear_pokemon()
            input("...")

        case '2':
            limpiar_pantalla()
            print("POKEMONS CARGADOS EN EL MAPA")
            print("====================================================================================")
            mapa_juego = mapa.Mapa(5)
            mapa_juego.mostrarMapaDetallado()
            input("...")

        case '3':
            limpiar_pantalla()
            print(f"Elegido: {pokemon_default.nombre}")
            print("====================================================================================")
            nombre = input("Selecciona tu nuevo pokemon de combate: ")
            nuevo_pokemon = cambiar_pokemon_default(nombre)

            if nuevo_pokemon:
                pokemon_default = nuevo_pokemon
            
            input("...")

        case '4':
            map_loop = True
            while map_loop:
                limpiar_pantalla()
                print("EXPLORACIÓN DE MAPA")
                print("====================================================================================")
                print("Arriba: w | Izquierda: a | Derecha: d | Abajo: s | Capturar: e | Combatir: f | Atrás: 0")
                print("====================================================================================")
                pokemon_enemigo = mapa_juego.coordenada_pokemon(jugador.x, jugador.y)
                mapa_juego.mostrarMapaDetallado()
                print("====================================================================================")
                print(f"Pokemon seleccionado: {pokemon_default.nombre}")
                print(f"Posición de Jugador: ({jugador.x}, {jugador.y})")
                print("====================================================================================")
                map_accion = input("Acción => ")
                match map_accion:
                    case '0':
                        map_loop = False
                        break

                    case 'w':
                        jugador.moverArriba()
                        if jugador.y > 4:
                            input("Límite del mapa alcanzado!")
                            jugador.y -= 1
                    
                    case 'a':
                        jugador.moverIzquierda()
                        if jugador.x < 0:
                            input("Límite del mapa alcanzado!")
                            jugador.x += 1

                    case 'd':
                        jugador.moverDerecha()
                        if jugador.x > 4:
                            input("Límite del mapa alcanzado!")
                            jugador.x -= 1

                    case 's':
                        jugador.moverAbajo()
                        if jugador.y < 0:
                            input("Límite del mapa alcanzado!")
                            jugador.y += 1

                    case 'e':
                        pokemon_enemigo_nombre = mapa_juego.coordenada_pokemon(jugador.x, jugador.y)[1]

                        for p in almacen_Pokemons:
                            if p.nombre == pokemon_enemigo_nombre:
                                jugador.capturar_pokemon(pokemon_default.ataque, p.defensa, p.nombre)

                                break               

                        input("Presiona Enter para continuar...")

                    case 'f':
                        pokemon_enemigo_nombre = mapa_juego.coordenada_pokemon(jugador.x, jugador.y)[1]

                        for p in almacen_Pokemons:
                            if p.nombre == pokemon_enemigo_nombre:
                                limpiar_pantalla()
                                jugador.combate(pokemon_default, p)

                                break