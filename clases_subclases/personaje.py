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

    def capturar_pokemon(self, pokemon):
        print("a")