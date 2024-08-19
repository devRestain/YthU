import streamlit as st

def Sidebar():
    with st.sidebar:
        reset = st.button(
            label= "RESET",
            use_container_width= True
        )
        if reset:
            st.session_state.clear()
            st.rerun()