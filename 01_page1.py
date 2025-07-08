# page1.py
import streamlit as st
import pandas as pd
import numpy as np

def show():
    st.title("ページ1")
    st.write("これはページ1のコンテンツです。")
    
    # サンプルコンテンツ
    st.subheader("データ表示例")
    
    data = pd.DataFrame({
        'カテゴリ': ['A', 'B', 'C', 'D'],
        '値': [23, 45, 56, 78]
    })
    st.dataframe(data)
    st.bar_chart(data.set_index('カテゴリ'))
    
    if st.button("ホームに戻る", key="page1_home"):
        st.session_state.page = 'home'
        st.rerun()

https://prod.liveshare.vsengsaas.visualstudio.com/join?D3ACF87ECF5ECCC63D077CC34B92F291A210
