from typing import List


class FlowerSpec:
    def __init__(self, species: str, size: str, max_qty: int):
        self.species = species
        self.size = size
        self.max_qty = max_qty

    def __repr__(self):
        return f"FlowerSpec(species={self.species}, size={self.size}, max_qty={self.max_qty})"

    def __str__(self):
        return f"{self.species} ({self.size}) - Max Qty: {self.max_qty}"

    def __eq__(self, other):
        if not isinstance(other, FlowerSpec):
            return NotImplemented
        return (self.species == other.species and
                self.size == other.size and
                self.max_qty == other.max_qty)

    def __hash__(self):
        return hash((self.species, self.size, self.max_qty))


class BouquetDesign:
    def __init__(self, name: str, flower_size: str, total_qty: int, flowers: List[FlowerSpec]):
        self.flowers = flowers
        self.name = name
        self.flower_size = flower_size
        self.total_qty = total_qty

    def __repr__(self):
        return (f"BouquetDesign(name={self.name}, flower_size={self.flower_size}, "
                f"total_qty={self.total_qty}, flowers={self.flowers})")

    def __str__(self):
        return f"{self.name} ({self.flower_size}) - Total: {self.total_qty} Flowers: {', '.join(str(f) for f in self.flowers)}"

    def __eq__(self, other):
        if not isinstance(other, BouquetDesign):
            return NotImplemented
        return (self.name == other.name and
                self.flower_size == other.flower_size and
                self.total_qty == other.total_qty and
                self.flowers == other.flowers)

    def __hash__(self):
        return hash((self.name, self.flower_size, self.total_qty, tuple(self.flowers)))
