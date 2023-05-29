import requests
import pandas as pd

def cor(name,df):

    name_list=name
    base= pd.DataFrame({'銘柄名': []})
    base.index.name="コード"

    for i in name_list:
        x=i.replace(".JP","")
        df1=df.loc[df.index == int(x)]
        base=pd.concat([base,df1])
    return base
