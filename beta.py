import datetime
from pandas_datareader import data
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def beta(datam,nikkei_df,s,e):
    selected = ["^NKX"]
    #株価データダウンロード
    #stooq = data.DataReader(selected,"stooq", start=s, end=e)
    stooq=nikkei_df
    data1 = stooq["Close"]

    data0=datam
    data1= pd.concat([data1,data0],axis=1).sort_values(by='Date',ascending=True)

    data2 = data1.pct_change()
    data3 = data2.iloc[::-1]
    data4 = data3.dropna()

    x = data4[selected[0]].values.reshape(-1,1)
    y = data4["Close"].values.reshape(-1,1)

    model_lr = LinearRegression()
    model_lr.fit(x,y)


    df1=stooq
    df2=data0

    df3=(df2["Close"] - df2["Close"].values.min()) / (df2["Close"].values.max() - df2["Close"].values.min())
    df4=(df1["Close"] - df1["Close"].values.min()) / (df1["Close"].values.max() - df1["Close"].values.min())

    plt.figure(figsize=(12,4))
    plt.title("Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)

    plt.plot(df3, label="Prise")
    plt.plot(df4, label="Nikkei")

    plt.legend()
    return plt,'%.3f' %model_lr.coef_
    #print('%.3f' %model_lr.coef_)
