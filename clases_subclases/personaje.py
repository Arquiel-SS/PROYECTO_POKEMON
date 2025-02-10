import time

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