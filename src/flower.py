
class Flower:
    def __init__(self, species:str, size: str):
        self.species = species
        self.size = size

    def __str__(self):
        return f"{self.species}{self.size}"
