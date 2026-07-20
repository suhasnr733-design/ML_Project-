import pandas as pd
from pathlib import Path
p=Path('cleaned_df.csv')
encs=['utf-8','utf-16','utf-16le','utf-16be','latin1','cp1252']
for e in encs:
    try:
        df=pd.read_csv(p,encoding=e,nrows=0)
        print('encoding',e)
        print(list(df.columns))
        break
    except Exception as ex:
        print('fail',e,str(ex))
