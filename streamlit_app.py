import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ページ関数を同一ファイル内で定義
def show_page1():
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
        st.experimental_rerun()  # 別の方法でページを更新

def show_page2():
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
        st.experimental_rerun()  # 別の方法でページを更新

def show_home():
    st.title("ホームページ")
    st.write("ページを選択してください。")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 ページ1へ", key="goto_page1"):
            st.session_state.page = 'page1'
            st.experimental_rerun()
        st.write("データ可視化のページ")
    
    with col2:
        if st.button("🎯 ページ2へ", key="goto_page2"):
            st.session_state.page = 'page2'
            st.experimental_rerun()
        st.write("インタラクティブなページ")

def main():
    # ページ状態の初期化
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # 現在のページ表示
    if st.session_state.page == 'home':
        show_home()
    elif st.session_state.page == 'page1':
        show_page1()
    elif st.session_state.page == 'page2':
        show_page2()

if __name__ == "__main__":
