from unittest import TestCase

from bouquet_design import BouquetDesign
from bouquet_maker import BouquetMaker


class TestBouquetMaker(TestCase):
    bouquet_design_1 = BouquetDesign('A', 'L', 3, {"aL": 2, "bL": 2})
    bouquet_design_2 = BouquetDesign('B', 'S', 2, {"aS": 2})

    def test_match(self):
        bouquet_maker = BouquetMaker()
        bouquet_maker.bouquet_designs = [self.bouquet_design_1, self.bouquet_design_2]
        bouquet_maker.flower_count = {
            "aS": 1,
            "aL": 2,
            "bL": 2,
        }
        bouquet = bouquet_maker.match()
        if bouquet:
            self.assertEqual("AL2a1b",str(bouquet))
        else:
            self.fail("Bouquet should have been matched but was None")
