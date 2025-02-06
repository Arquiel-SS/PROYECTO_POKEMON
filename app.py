import os, random, time
from clases_subclases import pokemon, mapa, personaje

# Importación de Pokemons
almacen_Pokemons = []

with open("listado_pokemons.txt") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")  # Eliminamos espacios y dividimos por comas
        pokemon_formateado = [[datos[0]], [datos[1]], [int(datos[2])], [int(datos[3])]]
        almacen_Pokemons.append(pokemon_formateado)

# Funciones de utilidad / Generales
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def informar_carga_pokemons():
    Planta = 0
    Agua = 0
    Fuego = 0
    Volador = 0

    for pokemon in almacen_Pokemons:
        tipo = pokemon[1][0]
        match tipo:
            case 'Planta':
                Planta += 1
            case 'Agua':
                Agua += 1
            case 'Fuego':
                Fuego += 1
            case 'Volador':
                Volador += 1

    print("POKEMONS CARGADOS EN EL MAPA")
    print("==============================")
    print(f"Pokémon Planta: {Planta}")
    print(f"Pokémon Agua: {Agua}")
    print(f"Pokémon Fuego: {Fuego}")
    print(f"Pokémon Voladores: {Volador}")
    print("==============================")

def cambiar_pokemon_default(nombre):
    for p in almacen_Pokemons:
        if p[0][0] == nombre:
            pokemon_default = pokemon.Pokemon(p[0][0], p[1][0], p[2][0], p[3][0], 100)
            return pokemon_default
    
    print("Pokemon no encontrado.")
    return False

def crear_pokemon():
        nombre = input("Nombre del pokemon: ")
        tipo = input("Tipo del pokemon (Planta, Agua, Fuego, Volador): ")
        atq = int(input("ATQ: "))
        defense = int(input("DEF: "))
        ps = int(input("PS: "))

        pokemon_personalizado = pokemon.Pokemon(nombre, tipo, atq, defense, ps)
        almacen_Pokemons.append([[pokemon_personalizado.nombre],[pokemon_personalizado.tipo], [pokemon_personalizado.ataque],[pokemon_personalizado.defensa], [pokemon_personalizado.ps]])

# Simulación de carga
limpiar_pantalla()
print("¡Bienvenido al Simulador de Entrenador Pokémon!")
time.sleep(1)
print("Se ha generado un mapa con Pokémon aleatorios")
time.sleep(1)
print("¡Prepárate para explorarlo!")
time.sleep(3)
limpiar_pantalla()
print("Cargando pokemons...")
time.sleep(0.2)
limpiar_pantalla()
print("Cargando pokemons.....")
time.sleep(0.5)
limpiar_pantalla()
print("Cargando pokemons.......")
time.sleep(0.2)
limpiar_pantalla()
print("Cargando pokemons.........")
time.sleep(0.7)
limpiar_pantalla()
print("Cargando pokemons...........")
time.sleep(1)

# Loop del juego
jugador = personaje.Jugador(0, 0, 'Gabriel')
prueba = pokemon.Pokemon('Prueba', 'Volador', 50, 70, 100)
pokemon_default = pokemon.Pokemon(almacen_Pokemons[0][0], almacen_Pokemons[0][1], almacen_Pokemons[0][2], almacen_Pokemons[0][3], 100)

mapa_juego = mapa.Mapa(5)

Menu = True
while Menu:
    limpiar_pantalla()
    informar_carga_pokemons()
    print("1. Añadir un pokemon personalizado")
    print("2. Ver pokemons cargados")
    print(f"3. Elegir pokemon de combate (Default: {pokemon_default.nombre})")
    print("4. Acceder al mapa")
    print("0. Salir")
    print("==============================")
    accion = input("Accion => ")
    match accion:
        case '0':
            print("Recibido")
            Menu = False

        case '1':
            limpiar_pantalla()
            print("BIENVENIDO A CREAR TU POKEMON")
            print("===============================")
            crear_pokemon()
            mapa_juego = mapa.Mapa(5)  
            input("...")

        case '2':
            limpiar_pantalla()
            print("POKEMONS CARGADOS EN EL MAPA")
            print("==============================")
            mapa_juego.mostrarMapaDetallado()
            input("...")

        case '3':
            limpiar_pantalla()
            print(f"Elegido: {pokemon_default.nombre}")
            print("===============================")
            nombre = input("Selecciona tu nuevo pokemon de combate: ")
            nuevo_pokemon = cambiar_pokemon_default(nombre)

            if nuevo_pokemon:
                pokemon_default = nuevo_pokemon
            
            input("...")