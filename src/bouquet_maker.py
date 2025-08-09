import collections

from bouquet import Bouquet
from bouquet_design import BouquetDesign
from bouquet_design_parser import BouquetDesignParser


class BouquetMaker:
    def __init__(self):
        self.bouquet_designs: list[BouquetDesign] = []
        self.bouquet_design_parser = BouquetDesignParser()
        self.bouquets = []
        self.flower_count: dict = collections.defaultdict(int)

    def run(self):
        print("Bouquet Maker is running...")

        print("Please enter bouquet designs (type Ctrl+C to exit):")
        try:
            self.bouquet_design_loop()

            self.flower_match_loop()

        except EOFError:
            print("EOFError encountered. Exiting bouquet maker.")

    def flower_match_loop(self):
        while True:
            user_input = input()
            if not user_input.strip():
                print("No input received")
                continue
            if len(user_input.strip()) < 2:
                print("Flower input must be at least 2 characters long (species and size).")
                continue
            if user_input.strip()[1] not in ['S', 'L']:
                print("Flower size must be 'S' or 'L'.")
                continue
            if not (user_input.strip()[0].isalpha() and user_input.strip()[0].islower()):
                print("Flower species must be a lowercase alphabetic character.")
                continue
            flower = user_input.strip()
            print(f"Received flower: {user_input}")

            self.flower_count[flower] += 1

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

    def match_bouquet(self, bouquet_design: BouquetDesign)-> bool:
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
        remaining_qty: int = bouquet_design.total_qty

        # ensure at least 1 of each flower
        for flower in bouquet_design.flowers.keys():
            bouquet_flowers[flower] = 1
            remaining_qty -= 1
            self.flower_count[flower] -= 1

        for flower,max_qty in bouquet_design.flowers.items():
            if remaining_qty <= 0:
                break

            available = self.flower_count[flower]
            allowed = max_qty - 1
            to_add = min(available, allowed, remaining_qty)

            bouquet_flowers[flower] += to_add
            remaining_qty -= to_add
            self.flower_count[flower] -= to_add

        bouquet = Bouquet(bouquet_design, bouquet_flowers)
        print(f"Bouquet {bouquet_design.name} successfully matched.")
        return bouquet
