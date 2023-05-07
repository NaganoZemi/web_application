import streamlit as st
import pandas as pd
import eff
import matplotlib.pyplot as plt
import price
import nikkei
import beta
import cor
import result

st.title("株式投資ポートフォリオ提案")


name = st.text_input('証券コードをコンマ区切りで入力してください(例：xxxx.JP,yyyy.JP,zzzz.JP)')
name_list=name.split(",")
s=st.text_input('計測開始日を入力してください(mm/dd/yy)')
e=st.text_input('計測終了日を入力してください(mm/dd/yy)')
money=st.text_input('投資金額を入力してください(万)')
button = st.button('計算開始')
if button==True:
    st.header('企業一覧')
    dfn=cor.cor(name_list)
    st.table(dfn)
    st.header('効率的フロンティア')
    plta,sharp,weight,df=eff.eff(name_list,s,e)
    st.write(sharp)
    st.pyplot(plta)
    st.header('提案するポートフォリオの価格変動')
    pltp,stock_data=price.price(name_list,weight,df)
    st.pyplot(pltp)
    st.header('日経平均との累積リターンの比較')
    pltn,nikkeidf=nikkei.nikkei(stock_data,s,e)
    st.pyplot(pltn)
    st.header("市場β値")
    pltb,beta1=beta.beta(stock_data,nikkeidf,s,e)
    st.text("市場β値："+beta1)
    st.subheader("日経平均株価との価格推移比較")
    st.pyplot(pltb)
    st.header("購入株数")
    result_df=result.result(money,name_list,weight,dfn)
    st.table(result_df)
