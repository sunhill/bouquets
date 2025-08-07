from bouquet_design_parser import BouquetDesignParser
from flower import Flower

class BouquetMaker:
    def __init__(self):
        self.bouquet_designs = []
        self.bouquet_design_parser = BouquetDesignParser()
        self.flowers = []
        self.boquets = []

    def run(self):
        print("Bouquet Maker is running...")

        print("Please enter bouquet designs (type Ctrl+C to exit):")

# designs input loop
        while True:
            user_input = input()
            if not user_input.strip():
                break
            print(f"Received bouquet design: {user_input}")
            self.bouquet_designs.append(self.bouquet_design_parser.parse_design_string(user_input))

# flowers input loop
        while True:
            user_input = input()
            print(f"Received flower: {user_input}")
            flower: Flower = self.bouquet_design_parser.parse_flower_string(user_input)

            self.flowers.append(flower)
            # TODO match stage
