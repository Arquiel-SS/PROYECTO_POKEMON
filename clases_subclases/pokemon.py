import time

class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.ps = ps

    def get_nombre(self):
        return self.nombre
    
    def get_tipo(self):
        return self.tipo
    
    def get_ataque(self):
        return self.ataque
    
    def get_defensa(self):
        return self.defensa
    
    def get_ps(self):
        return self.ps
    
    def set_ps(self, nuevo_ps):
        self.ps = nuevo_ps

    def ataque_normal(self, enemigo):
        print(f"¡{self.nombre} usa placaje!")
        dmg = self.ataque - enemigo.defensa
        time.sleep(1)

        if dmg < 0:
            print(f"¡El ataque ha sido demasiado débil!")
            dmg = 0

        else:
            enemigo.ps -= dmg

        print(f"{dmg} de daño")
        print("====================================================================================")


    def mostrar_info(self):
        print("-------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        match self.tipo:
            case 'Planta':
                mensaje = f'Ten cuidado con el tipo Fuego! Acabarás quemado de tanta pelea'

            case 'Fuego':
                mensaje = f'Ten cuidado con el tipo Agua! Te regarán a guantazos'

            case 'Agua':
                mensaje = f'Ten cuidado con el tipo Planta! Te van a dejar plantado en el sitio'

            case 'Volador':
                mensaje = f'Mandas a los demás a volar de un galletazo'


        print(f"Comentario: {mensaje}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"PS: {self.ps}")
        print("-------------------------")

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)

    def ataque_especial(self, enemigo):
        print(f"¡{self.nombre} usa un ataque especial de tipo Planta!")
        dmg = (self.ataque * 2) - enemigo.defensa
        time.sleep(1)
        if dmg < 0:
            print(f"¡El ataque ha sido demasiado débil!")
            dmg = 0
        
        else:
            enemigo.ps -= dmg

        print(f"{dmg} de daño")
        print("====================================================================================")



class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)

    def ataque_especial(self, enemigo):
        print(f"¡{self.nombre} usa un ataque especial de tipo Agua!")
        dmg = (self.ataque * 2) - enemigo.defensa
        time.sleep(1)
        if dmg < 0:
            print(f"¡El ataque ha sido demasiado débil!")
            dmg = 0
        
        else:
            enemigo.ps -= dmg

        print(f"{dmg} de daño")
        print("====================================================================================")


class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)

    def ataque_especial(self, enemigo):
        print(f"¡{self.nombre} usa un ataque especial de tipo Fuego!")
        dmg = (self.ataque * 2) - enemigo.defensa
        time.sleep(1)
        if dmg < 0:
            print(f"¡El ataque ha sido demasiado débil!")
            dmg = 0

        else:
            enemigo.ps -= dmg

        print(f"{dmg} de daño")
        print("====================================================================================")

        

class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)

    def ataque_especial(self, enemigo):
        print(f"¡{self.nombre} usa un ataque especial de tipo Volador!")
        dmg = (self.ataque * 2) - enemigo.defensa
        time.sleep(1)
        if dmg < 0:
            print(f"¡El ataque ha sido demasiado débil!")
            dmg = 0
        
        else:
            enemigo.ps -= dmg

        print(f"{dmg} de daño")
        print("====================================================================================")
