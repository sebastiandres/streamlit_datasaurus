import streamlit as st
import importlib

# Set page configuration
st.set_page_config(layout="wide", page_title="Streamlitsaurus Rex",
                   page_icon="🦖",
                   initial_sidebar_state="expanded")

# Sidebar
page_dict = {
            "Welcome!": "00_why", 
            "What is a Datasaurus?": "01_intro", 
            "Where can I see a Datasaurus?": "03_datasaurus", 
            "Can I have my own Datasaurus?": "04_custom", 
            "About": "05_about"}
st.sidebar.header("Navigation")
selected_page = st.sidebar.selectbox("Select page", page_dict.keys())
selected_module = page_dict[selected_page]

# Render the content
current_module = importlib.import_module(selected_module)
current_module.display_page()