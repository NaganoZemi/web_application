import requests
import pandas as pd

def cor(name):
    url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"
    r = requests.get(url)
    with open('data_j.xls', 'wb') as output:
        output.write(r.content)
    df = pd.read_excel("./data_j.xls", index_col=1)[["銘柄名"]]

    name_list=name
    base= pd.DataFrame({'銘柄名': []})
    base.index.name="コード"

    for i in name_list:
        x=i.replace(".JP","")
        df1=df.loc[df.index == int(x)]
        base=pd.concat([base,df1])
    return base
