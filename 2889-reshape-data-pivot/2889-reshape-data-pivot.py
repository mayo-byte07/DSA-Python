import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Use pivot to reshape the DataFrame and leave 'month' as the index
    return weather.pivot(index='month', columns='city', values='temperature')