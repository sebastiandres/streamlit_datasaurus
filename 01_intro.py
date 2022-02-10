import streamlit as st

def display_page():
    # Set title
    st.title("Intro")

    # Set header
    st.header("What is this mess")

    # Content
    st.markdown("""
    Describe:
    - Importance of visualization
    - Anscombe's paper
    - Datasaurius
    - How we want to make fun to visualize
    """)