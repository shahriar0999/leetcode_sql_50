import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filterd = products[(products['low_fats']=='Y') & (products['recyclable'] == 'Y')]
    return filterd[['product_id']]
    
