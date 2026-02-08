import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result_table  = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return result_table[['name', 'population', 'area']]
