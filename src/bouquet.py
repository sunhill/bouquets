from bouquet_design import BouquetDesign


class Bouquet:
    def __init__(self, design: BouquetDesign, flowers: dict[str, int]):
        self.design = design
        self.flowers = flowers

    def __str__(self):
        flower_string = ""
        for flower in self.flowers.keys():
            flower_string += f"{self.flowers[flower]}{flower[0:1]}"
        return f"{self.design.name}{self.design.flower_size}{flower_string}"
