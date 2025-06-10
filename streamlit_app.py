import streamlit as st
import page1
import page2

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.session_state.page == 'home':
        show_home()
    elif st.session_state.page == 'page1':
        page1.show()
    elif st.session_state.page == 'page2':
        page2.show()

def show_home():
    st.title("ホームページ")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("ページ1へ"):
            st.session_state.page = 'page1'
            st.experimental_rerun()
    with col2:
        if st.button("ページ2へ"):
            st.session_state.page = 'page2'
            st.experimental_rerun()

if __name__ == "__main__":
    main()

