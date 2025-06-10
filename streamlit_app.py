# main.py
import streamlit as st

# ページ関数を同一ファイル内で定義
def show_page1():
    st.title("ページ1")
    st.write("これはページ1のコンテンツです。")
    
    # サンプルコンテンツ
    st.subheader("データ表示例")
    import pandas as pd
    import numpy as np
    
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
    
    # サンプルコンテンツ
    st.subheader("インタラクティブ要素")
    
    name = st.text_input("お名前を入力してください")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    
    if name:
        st.success(f"こんにちは、{name}さん！ {age}歳ですね。")
    
    # グラフ例
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * age / 25  # 年齢に応じて振幅を変更
    
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
            st.rerun()
        st.write("データ可視化のページ")
    
    with col2:
        if st.button("🎯 ページ2へ", key="goto_page2"):
            st.session_state.page = 'page2'
            st.rerun()
        st.write("インタラクティブなページ")

def main():
    # ページ状態の初期化
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # サイドバーでナビゲーション
    st.sidebar.title("ナビゲーション")
    page_options = {
        'home': 'ホーム',
        'page1': 'ページ1',
        'page2': 'ページ2'
    }
    
    selected_page = st.sidebar.selectbox(
        "ページを選択",
        options=list(page_options.keys()),
        format_func=lambda x: page_options[x],
        index=list(page_options.keys()).index(st.session_state.page)
    )
    
    # サイドバーで選択されたページに移動
    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()
    
    # 現在のページ表示
    if st.session_state.page == 'home':
        show_home()
    elif st.session_state.page == 'page1':
        show_page1()
    elif st.session_state.page == 'page2':
        show_page2()

if __name__ == "__main__":
    main()
