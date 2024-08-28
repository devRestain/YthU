import streamlit as st


def Setting(name):
    st.set_page_config(
        page_title="We Always YthU",
    )
    st.title(
        body="We Always YthU",
    )
    st.subheader(
        body=name,
    )
    if "test" not in st.session_state:
        st.session_state.test = ""
