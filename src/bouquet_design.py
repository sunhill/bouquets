class BouquetDesign:
    def __init__(self, name: str, flower_size: str, total_qty: int, flowers: dict):
        self.flowers: dict[str, int] = flowers
        self.name = name
        self.flower_size = flower_size
        self.total_qty = total_qty

    def __repr__(self):
        return (f"BouquetDesign(name={self.name}, flower_size={self.flower_size}, "
                f"total_qty={self.total_qty}, flowers={self.flowers})")

    def __str__(self):
        return f"{self.name} ({self.flower_size}) - Total: {self.total_qty} Flowers: {', '.join(str(f) for f in self.flowers)}"
