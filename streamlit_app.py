# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def show_page1():
    st.title("ページ1")
    st.write("これはページ1のコンテンツです。")
    
    # ここに st.subheader を配置（関数内なのでOK）
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

def show_page2():
    st.title("ページ2")
    st.write("これはページ2のコンテンツです。")
    
    # ここに st.subheader を配置（関数内なのでOK）
    st.subheader("インタラクティブ要素")
    
    name = st.text_input("お名前を入力してください")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    
    if name:
        st.success(f"こんにちは、{name}さん！ {age}歳ですね。")
    
    # グラフ例
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * age / 25
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f'{name}さんの波形（年齢: {age}）')
    st.pyplot(fig)
    
    if st.button("ホームに戻る", key="page2_home"):
        st.session_state.page = 'home'
        st.rerun()

def show_home():
    st.title("ホームページ")
    st.write("ページを選択してください。")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 ページ1へ", key="goto_page1"):
            st.session_state.page = 'page1'
            st.rerun()  # この st.rerun() も関数内なのでOK
        st.write("データ可視化のページ")
    
    with col2:
        if st.button("🎯 ページ2へ", key="goto_page2"):
            st.session_state.page = 'page2'
            st.rerun()  # この st.rerun() も関数内なのでOK
        st.write("インタラクティブなページ")

def main():
    # ページ設定（アプリの最初に一度だけ実行）
    st.set_page_config(
        page_title="マルチページアプリ",
        page_icon="🚀",
        layout="wide"
    )
    
    # ページ状態の初期化
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # サイドバーでナビゲーション
    with st.sidebar:
        st.title("🧭 ナビゲーション")
        
        # 現在のページを表示
        st.info(f"現在のページ: {st.session_state.page}")
        
        # ページ選択ボタン
        if st.button("🏠 ホーム", key="nav_home"):
            st.session_state.page = 'home'
            st.rerun()
        
        if st.button("📊 ページ1", key="nav_page1"):
            st.session_state.page = 'page1'
            st.rerun()
        
        if st.button("🎯 ページ2", key="nav_page2"):
            st.session_state.page = 'page2'
            st.rerun()
    
    # 現在のページに応じて表示
    if st.session_state.page == 'home':
        show_home()
    elif st.session_state.page == 'page1':
        show_page1()
    elif st.session_state.page == 'page2':
        show_page2()
    else:
        # 不正なページの場合はホームに戻す
        st.session_state.page = 'home'
        st.rerun()

# メイン実行部分
if __name__ == "__main__":
    main()
