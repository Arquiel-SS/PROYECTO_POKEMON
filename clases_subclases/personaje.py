import time, os

def limpiar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moverIzquierda(self):
        self.x -= 1

    def moverDerecha(self):
        self.x += 1

    def moverArriba(self):
        self.y += 1

    def moverAbajo(self):
        self.y -= 1

class Jugador(Personaje):
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre = nombre

    def capturar_pokemon(self, ataque_j, defensa_p, nombre):
        print(f"Se ha lanzado una pokeball a {nombre}...........")
        time.sleep(1.5)
        if ataque_j > defensa_p:
            print(f"Has capturado a {nombre}!")

        else:
            print(f"{nombre} se ha escapado!")

    def combate(self, pokemon_j, pokemon_enemigo):
        print(f"¡El jugador {self.nombre} ha iniciado un enfrentamiento contra un {pokemon_enemigo.nombre} salvaje!")
        time.sleep(2.5)
        combate = True

        while combate:
            limpiar_pantalla()
            print("====================================================================================")
            print(f"{pokemon_j.nombre} | Ataque: {pokemon_j.ataque} | Defensa: {pokemon_j.defensa} | PS: {pokemon_j.ps}")
            print(f"{pokemon_enemigo.nombre} | Ataque: {pokemon_enemigo.ataque} | Defensa: {pokemon_enemigo.defensa} | PS: {pokemon_enemigo.ps}")
            print("====================================================================================")
            print("1. Atacar")
            print("2. Usar ataque especial")
            opcion = input("Elige una acción: ")
        
            match opcion:
                case '1':
                    pokemon_j.ataque_normal(pokemon_enemigo)
                case '2':
                    pokemon_j.ataque_especial(pokemon_enemigo)
            
            if pokemon_enemigo.ps <= 0:
                print(f"¡{pokemon_enemigo.nombre} ha sido derrotado!")
                input("Combate terminado.....")
                combate = False
                break

            pokemon_enemigo.ataque_normal(pokemon_j)

            if pokemon_j.ps <= 0:
                print(f"¡{pokemon_j.nombre} ha sido derrotado!")
                input("Combate terminado.....")
                combate = False
                break

            input("Turno terminado...")