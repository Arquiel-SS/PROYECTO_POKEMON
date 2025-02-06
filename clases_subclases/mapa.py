import random

# Importación de Pokemons
almacen_Pokemons = []

with open("listado_pokemons.txt") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")  # Eliminamos espacios y dividimos por comas
        pokemon_formateado = [[datos[0]], [datos[1]], [int(datos[2])], [int(datos[3])]]
        almacen_Pokemons.append(pokemon_formateado)

class Mapa:
    def __init__(self, lado):
        self.lado = lado
        self.mapa = [
            [f"({x},{y}): {almacen_Pokemons[random.randint(0, len(almacen_Pokemons) - 1)][0]}" for y in range(lado)] 
                for x in range(lado)
        ]
    
    def coordenada(self, x, y):
        print(self.mapa[x][y])
    
    def mostrarMapa(self):
        for fila in self.mapa:
            # Mostrar solo las coordenadas, separando la cadena por ":"
            print(" | ".join([item.split(":")[0] for item in fila]) + " ")

    def mostrarMapaDetallado(self):
        for fila in self.mapa:
            print(" | ".join(fila) + " ")  # Imprimir cada fila formateada