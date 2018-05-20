import os
import pandas as pd
from datetime import datetime
try:
    import pandas_datareader.data as web
except ImportError:
    # bug-fix for missing 'is_list_like'
    pd.core.common.is_list_like = pd.api.types.is_list_like
    import pandas_datareader.data as web

def get_market_data(symbol='CBRX', start=None, end=None, calc=None):
    df = web.DataReader(symbol, 'morningstar', start, end)