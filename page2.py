# page2.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def show():
    st.title("ページ2")
    st.write("これはページ2のコンテンツです。")
    
    # サンプルコンテンツ
    st.subheader("インタラクティブ要素")
    
    name = st.text_input("お名前を入力してください")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    
    if name:
        st.success(f"こんにちは、{name}さん！ {age}歳ですね。")
    
    # グラフ例
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * age / 25  # 年齢に応じて振幅を変更
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f'{name}さんの波形（年齢: {age}）')
    st.pyplot(fig)
    
    if st.button("ホームに戻る", key="page2_home"):
        st.session_state.page = 'home'
        st.rerun()
