import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ath = views[views['author_id'] == views['viewer_id']]
    un = ath['author_id'].sort_values().unique()
    return pd.DataFrame({'id': un})
