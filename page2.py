import streamlit as st

def show():
    st.title("ページ2")
    st.write("こちらはページ2の内容です。")
    if st.button("ホームに戻る"):
        st.session_state.page = 'home'
        st.experimental_rerun()

