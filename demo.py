from random import randint
class Obrero():
    def __init__(self):
        self.carisma = randint(-100,100)
        self.prestigio = randint(-100,100)
        self.recursos = randint(-100,100)
    def __str__(self):
        return f"<Obrero> => carisma:{self.carisma}, prestigio:{self.prestigio}, recursos:{self.recursos}"
    
from abc import ABC, abstractmethod
class AccionDeFuerza(ABC):
    @abstractmethod
    def __init__(self, costo, modificadores):
        self.costo = costo
        self.modificadores = modificadores
    @abstractmethod
    def resultado(self, *args, **kwargs):
        pass

class Manifestacion(AccionDeFuerza):
    def __init__(self,modificadores):
        super().__init__(100, modificadores)
    
    def resultado(self):
        if (randint(-10,10) + self.modificadores.get("carisma")) > 0:
            return True
        return False

class Paritaria(AccionDeFuerza):
    def __init__(self,modificadores):
        super().__init__(100, modificadores)
    
    def resultado(self):
        if (randint(-30,30) + self.modificadores.get("prestigio")) > 0:
            return True
        return False
    

for i in range(3):
    obrero = Obrero()
    manifestacion = Manifestacion(obrero.__dict__)
    paritaria = Paritaria(obrero.__dict__)

    print(f"En este run el obrero es => {obrero}")
    print(f"Obrero hace una manifestacion. Como obrero tiene carisma = {obrero.carisma}, la manifestacion modifica su probabilidad de éxito")
    print(f"El resultado de la manifestacion fue {manifestacion.resultado()}")
    print(f"Obrero negocia la paritaria. Como obrero tiene prestigio = {obrero.prestigio}, la negociacion modifica su probabilidad de éxito")
    print(f"El resultado de la paritaria fue {paritaria.resultado()}")
    print()