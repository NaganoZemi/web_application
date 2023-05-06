# ライブラリの読み込み
from pandas_datareader import data
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def nikkei(data0,start,end):
    df=data0
    df_sum=df.pct_change()
    cum_ret_d=(1+df_sum).cumprod()
    df_m = data.DataReader(["^NKX"],"stooq", start, end)
    df1=df_m['Close'].sort_index()
    df1_sum=df1.pct_change()
    cum_ret_d1=(1+df1_sum).cumprod()
    fig=plt.figure(figsize=(12,4))
    plt.plot(cum_ret_d,label="Price")
    plt.plot(cum_ret_d1,label="Nikkei")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend(loc = 'upper left')
    return plt,df_m
