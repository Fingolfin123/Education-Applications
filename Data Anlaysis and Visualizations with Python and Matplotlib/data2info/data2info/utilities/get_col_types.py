import pandas as pd
from datetime import datetime
#from pyzt import utc
from pandas.api.types import is_datetime64_any_dtype as is_datetime


#get column types

def getTypes(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col])        
            except ValueError:
                pass    
    #df[[column for column in df.columns if is_datetime(df[column])]]
    
    df_types = df.dtypes
    return df_types