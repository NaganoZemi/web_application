import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data

def price(x,y,master_df):
    symbols=x
    bigger=y

    df=master_df
    # カラムを銘柄名でリネーム
    df.columns = symbols

    # 各銘柄の株価に重みをかけ、ポートフォリオの株価を計算
    plt.clf()
    z = (df * bigger).sum(axis=1)
    z=z.to_frame(name='Close')
    z2=z.dropna()
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_title("aa")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid(True)
    ax.plot(z2["Close"])
    return fig,z2
