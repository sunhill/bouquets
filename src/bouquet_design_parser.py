import re

from bouquet_design import FlowerSpec, BouquetDesign
from flower import Flower


class BouquetDesignParser:
    """
    A parser for bouquet design strings.
    This class is used to parse bouquet design strings into a structured format.
    """

    @staticmethod
    def parse_design_string(design_str: str) -> BouquetDesign:
        """
        Create a BouquetDesign from a string representation.
        Example format: "AL1d2r3t"
        """
        if not design_str or len(design_str) < 6:
            raise ValueError("Design string must be at least 6 characters long")
        name = design_str[0]
        flower_size = design_str[1]

        # Find the last number before 't'
        match = re.search(r'(\d+)(?=t$)', design_str)
        if not match:
            raise ValueError("No total quantity found before 't'")
        total_qty = int(match.group(1))

        # Remove the trailing total_qty and 't' to get the flowers string
        flowers_str = design_str[2:match.start(1)]
        flowers = []
        flower_pattern = re.compile(r'(\d+)([a-z])')
        matches = flower_pattern.findall(flowers_str)
        if not matches:
            raise ValueError("No valid flower specifications found in the design string")
        for max_qty,species  in matches:
            flowers.append(Flower(species, int(max_qty)))

        return BouquetDesign(name, flower_size, total_qty, flowers)

    def parse_flower_string(self, flower_str) -> Flower:
        if len(flower_str) < 2:
            raise ValueError("Flower string must be at least 2 characters long")
        species = flower_str[0]
        size = flower_str[1]
        return Flower(species, size)




if __name__ == "__main__":
    # Example usage
    BouquetDesignParser.parse_design_string("AL1d2r3t")
