from bouquet import Bouquet
from bouquet_design import BouquetDesign
from bouquet_design_parser import BouquetDesignParser


class BouquetMaker:
    def __init__(self):
        self.bouquet_designs: list[BouquetDesign] = []
        self.bouquet_design_parser = BouquetDesignParser()
        self.bouquets = []
        self.flower_count: dict = {}  # Map to track available flowers by species

    def run(self):
        print("Bouquet Maker is running...")

        print("Please enter bouquet designs (type Ctrl+C to exit):")
        try:
            self.bouquet_design_loop()

            self.flower_loop()

        except EOFError:
            print("EOFError encountered. Exiting bouquet maker.")

    def flower_loop(self):
        while True:
            user_input = input()
            if not user_input.strip():
                break
            print(f"Received flower: {user_input}")
            flower = BouquetDesignParser.parse_flower_string(user_input)
            if not flower.species or not flower.size:
                print("Invalid flower input. Please provide a valid species and size.")
                continue
            flower = f"{flower.species}{flower.size}"

            # Check if the flower species is already in the count map
            if flower not in self.flower_count:
                self.flower_count[flower] = 0

            self.flower_count[flower] += 1

            for flower in self.flower_count.keys():
                print(f"Flower {flower} count: {self.flower_count[flower]}")

            bouquet = self.match()
            if bouquet:
                self.bouquets.append(bouquet)
                print(bouquet)

    def bouquet_design_loop(self):
        while True:
            user_input = input()
            if not user_input.strip():
                break
            print(f"Received bouquet design: {user_input}")
            self.bouquet_designs.append(self.bouquet_design_parser.parse_design_string(user_input))

    def match(self) -> Bouquet | None:

        for bouquet_design in self.bouquet_designs:
            bouquet_match = self.match_bouquet(bouquet_design)

            if bouquet_match:
                bouquet = self.make_bouquet(bouquet_design)
                print(f"Made bouquet {bouquet_design.name}, exiting loop")
                return bouquet

        return None

    def match_bouquet(self, bouquet_design: BouquetDesign):
        bouquet_match = True
        flower_count = 0
        for flower in bouquet_design.flowers.keys():
            if flower not in self.flower_count:
                print(f"Flower {flower} not available for bouquet {bouquet_design.name}")
                bouquet_match = False
                break
            if self.flower_count[flower] < 1:
                print(f"Not enough flowers available for bouquet {bouquet_design.name} of flower {flower}")
                bouquet_match = False
                break
            flower_count = flower_count + self.flower_count[flower]
        if bouquet_match and bouquet_design.total_qty > flower_count:
            print(f"Not enough flowers available for bouquet {bouquet_design.name}")
            bouquet_match = False
        return bouquet_match

    def make_bouquet(self, bouquet_design: BouquetDesign) -> Bouquet:
        bouquet_flowers: dict[str, int] = {}
        bouquet_total_remaining: int = bouquet_design.total_qty

        # ensure at least 1 of each flower
        for flower in bouquet_design.flowers.keys():
            bouquet_flowers[flower] = 1
            bouquet_total_remaining -= bouquet_flowers[flower]
            self.flower_count[flower] = self.flower_count[flower] - 1

        bouquet_flower_count = 0
        for flower in bouquet_design.flowers.keys():
            if bouquet_total_remaining <= 0:
                break
            flower_max_qty = bouquet_design.flowers[flower] - 1
            # if flower_max_qty is greater than the available flowers, use all available flowers
            if flower_max_qty > self.flower_count[flower]:
                if bouquet_total_remaining < self.flower_count[flower]:
                    # fill the bouquet
                    bouquet_flower_count += bouquet_total_remaining
                else:
                    # use all available flowers
                    bouquet_flower_count += self.flower_count[flower]
            else:
                if bouquet_total_remaining < flower_max_qty:
                    # fill the bouquet
                    bouquet_flower_count += bouquet_total_remaining
                else:
                    # use the maximum quantity
                    bouquet_flower_count += flower_max_qty


            bouquet_flowers[flower] += bouquet_flower_count
            bouquet_total_remaining -= bouquet_flower_count
            self.flower_count[flower] -= bouquet_flower_count

        bouquet = Bouquet(bouquet_design, bouquet_flowers)
        print(f"Bouquet {bouquet_design.name} successfully matched.")
        return bouquet
