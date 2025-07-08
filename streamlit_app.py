import streamlit as st
import sys

# Streamlitの動作確認
try:
    # セッション状態の初期化
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
except Exception as e:
    st.error(f"セッション状態の初期化エラー: {e}")
    st.error("このアプリは 'streamlit run filename.py' で実行してください")
    st.stop()

# ページ遷移関数
def navigate_to(page_name):
    try:
        st.session_state.current_page = page_name
        st.rerun()
    except Exception as e:
        st.error(f"ページ遷移エラー: {e}")

# ホームページ
def home_page():
    st.title("ホームページ")
    
    st.info("各ボタンをクリックして異なるページに移動できます")
    
    # 4つのボタンを2つずつ縦並びで表示
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("ページ1に移動", key="nav_page1"):
            navigate_to('page1')
        
        if st.button("ページ2に移動", key="nav_page2"):
            navigate_to('page2')
    
    with col2:
        if st.button("ページ3に移動", key="nav_page3"):
            navigate_to('page3')
        
        if st.button("設定ページ", key="nav_settings"):
            navigate_to('settings')

# ページ1
def page1():
    st.title("ページ1")
    st.success("ページ1へようこそ！")
    
    st.write("これはページ1の内容です。")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ホームに戻る", key="back_home_1"):
            navigate_to('home')
    with col2:
        if st.button("ページ2へ", key="to_page2_from_1"):
            navigate_to('page2')

# ページ2
def page2():
    st.title("ページ2")
    st.info("ページ2へようこそ！")
    
    st.write("これはページ2の内容です。")
    
    # 簡単なフォーム例
    with st.form("page2_form"):
        name = st.text_input("お名前を入力してください")
        age = st.number_input("年齢", min_value=0, max_value=120)
        submitted = st.form_submit_button("送信")
        
        if submitted:
            st.success(f"こんにちは、{name}さん！（{age}歳）")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ホームに戻る", key="back_home_2"):
            navigate_to('home')
    with col2:
        if st.button("ページ3へ", key="to_page3_from_2"):
            navigate_to('page3')

# ページ3
def page3():
    st.title("ページ3")
    st.warning("ページ3へようこそ！")
    
    st.write("これはページ3の内容です。")
    
    # チャート例
    try:
        import pandas as pd
        import numpy as np
        
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        
        st.line_chart(chart_data)
    except ImportError:
        st.warning("チャートの表示にはpandasとnumpyが必要です")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ホームに戻る", key="back_home_3"):
            navigate_to('home')
    with col2:
        if st.button("設定へ", key="to_settings_from_3"):
            navigate_to('settings')

# 設定ページ
def settings_page():
    st.title("設定ページ")
    st.error("設定ページへようこそ！")
    
    st.write("アプリケーションの設定を行います。")
    
    # 設定項目例
    theme = st.selectbox("テーマを選択", ["ライト", "ダーク", "オート"])
    notifications = st.checkbox("通知を有効にする", value=True)
    language = st.radio("言語", ["日本語", "English", "中文"])
    
    if st.button("設定を保存"):
        st.success("設定が保存されました！")
    
    if st.button("ホームに戻る", key="back_home_settings"):
        navigate_to('home')

# サイドバーにナビゲーション
st.sidebar.title("ナビゲーション")
st.sidebar.write(f"現在のページ: {st.session_state.current_page}")

if st.sidebar.button("ホーム"):
    navigate_to('home')
if st.sidebar.button("ページ1"):
    navigate_to('page1')
if st.sidebar.button("ページ2"):
    navigate_to('page2')
if st.sidebar.button("ページ3"):
    navigate_to('page3')
if st.sidebar.button("設定"):
    navigate_to('settings')

# メイン実行部分
def main():
    try:
        # 現在のページに応じて表示する内容を切り替え
        if st.session_state.current_page == 'home':
            home_page()
        elif st.session_state.current_page == 'page1':
            page1()
        elif st.session_state.current_page == 'page2':
            page2()
        elif st.session_state.current_page == 'page3':
            page3()
        elif st.session_state.current_page == 'settings':
            settings_page()
        else:
            # 不明なページの場合はホームに戻る
            navigate_to('home')
    except Exception as e:
        st.error(f"アプリケーションエラー: {e}")
        st.error("ページの読み込みに失敗しました")

# アプリケーションの実行
if __name__ == "__main__":
    main()