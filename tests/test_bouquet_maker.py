import pytest
from bouquet_design import BouquetDesign
from bouquet_maker3 import BouquetMaker

bouquet_design_1 = BouquetDesign('A', 'L', 3, {"aL": 2, "bL": 2})
bouquet_design_2 = BouquetDesign('B', 'S', 2, {"aS": 2})


@pytest.mark.parametrize(
    "bouquet_designs,flower_count,expected_bouquet,expected_flower_count",
    [
        ([bouquet_design_1, bouquet_design_2],
         {"aS": 1, "aL": 2, "bL": 2},
         "AL2a1b",
         {"aS": 1, "aL": 0, "bL": 1}
         ),
        ([bouquet_design_1, bouquet_design_2],
         {"aS": 2, "aL": 1, "bL": 1},
         "BS2a",
         {"aS": 0, "aL": 1, "bL": 1}
         ),
        ([bouquet_design_1, bouquet_design_2],
         {"aS": 0, "aL": 0, "bL": 0},
         None,
         {"aS": 0, "aL": 0, "bL": 0}
         ),
        ([bouquet_design_1, bouquet_design_2],
         {"aS": 1, "aL": 1, "bL": 1},
         None,
         {"aS": 1, "aL": 1, "bL": 1}
         ),
    ]
)
def test_match_parametrized(bouquet_designs, flower_count, expected_bouquet, expected_flower_count):
    bouquet_maker = BouquetMaker()
    bouquet_maker.bouquet_designs = bouquet_designs
    bouquet_maker.flower_count = flower_count.copy()
    bouquet = bouquet_maker.match()
    if expected_bouquet is not None:
        assert bouquet is not None
        assert str(bouquet) == expected_bouquet
        assert bouquet_maker.flower_count == expected_flower_count
    else:
        assert bouquet is None
        assert bouquet_maker.flower_count == expected_flower_count
