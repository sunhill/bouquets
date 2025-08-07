import re

from bouquet_design import BouquetDesign


class BouquetDesignParser:
    """
    A parser for bouquet design strings.
    This class is used to parse bouquet design strings into a structured format.
    """

    @staticmethod
    def parse_design_string(design_str: str) -> BouquetDesign:
        """
        Create a BouquetDesign from a string representation.
        Example format: "AL1d2r3"
        """
        if not design_str or len(design_str) < 5:
            raise ValueError("Design string must be at least 5 characters long")
        name = design_str[0]
        flower_size = design_str[1]

        # Find the last number for the total quantity
        match = re.search(r'(\d+$)', design_str)
        if not match:
            raise ValueError("No total quantity found")
        total_qty = int(match.group(1))

        # Remove the trailing total_qty to get the flowers string
        flowers_str = design_str[2:match.start(1)]
        flowers: dict[str, int] = {}
        flower_pattern = re.compile(r'(\d+)([a-z])')
        matches = flower_pattern.findall(flowers_str)
        if not matches:
            raise ValueError("No valid flower specifications found in the design string")
        for max_qty, species in matches:
            flower = f"{species}{flower_size}"
            flowers[flower] = int(max_qty)

        return BouquetDesign(name, flower_size, total_qty, flowers)


if __name__ == "__main__":
    # Example usage
    BouquetDesignParser.parse_design_string("AL1d2r3t")
