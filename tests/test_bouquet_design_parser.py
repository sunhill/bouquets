from unittest import TestCase

from bouquet_design import BouquetDesign
from bouquet_design_parser import BouquetDesignParser


class TestBouquetDesignParser(TestCase):
    def test_parse_design_from_string(self):
        design_str = "AL1d2r3"
        try:
            design = BouquetDesignParser.parse_design_string(design_str)
            self.assertIsInstance(design, BouquetDesign)
            self.assertEqual(design.name, "A")
            self.assertEqual(design.flower_size, "L")
            self.assertEqual(design.total_qty, 3)
            self.assertEqual(len(design.flowers), 2)
            self.assertEqual(design.flowers["dL"], 1)
            self.assertEqual(design.flowers["rL"], 2)
        except ValueError as e:
            print(f"Error: {e}")

    def test_parse_design_with_multiple_digit_total(self):
        design_str = "AL1d2r30"
        try:
            design = BouquetDesignParser.parse_design_string(design_str)
            self.assertIsInstance(design, BouquetDesign)
            self.assertEqual(design.name, "A")
            self.assertEqual(design.flower_size, "L")
            self.assertEqual(design.total_qty, 30)
            self.assertEqual(len(design.flowers), 2)
            self.assertEqual(design.flowers["dL"], 1)
            self.assertEqual(design.flowers["rL"], 2)
        except ValueError as e:
            print(f"Error: {e}")

    def test_parse_design_with_multiple_digit_total_and_flowers(self):
        design_str = "AL11d22r30"
        try:
            design = BouquetDesignParser.parse_design_string(design_str)
            self.assertIsInstance(design, BouquetDesign)
            self.assertEqual(design.name, "A")
            self.assertEqual(design.flower_size, "L")
            self.assertEqual(design.total_qty, 30)
            self.assertEqual(len(design.flowers), 2)
            self.assertEqual(design.flowers["dL"],11)
            self.assertEqual(design.flowers["rL"],  22)
        except ValueError as e:
            print(f"Error: {e}")

    def test_parse_invalid_design_string(self):
        invalid_designs = [
            "AL1d2r3t5x",  # Invalid character at the end
            "AL1dr3t5x",  # No quantity for 'r'
            "A",  # Too short
            "",  # Empty string
            "AL1d2r3t5xd"  # Extra characters at the end
        ]

        for design_str in invalid_designs:
            with self.subTest(design_str=design_str):
                with self.assertRaises(ValueError):
                    BouquetDesignParser.parse_design_string(design_str)
