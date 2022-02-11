import streamlit as st
import importlib

# Set page configuration
st.set_page_config(layout="wide", page_title="Streamlitsaurus Rex",
                   page_icon="🦖",
                   initial_sidebar_state="collapsed")

# Sidebar
page_dict = {
            "Why": "00_why", 
            "Intro": "01_intro", 
            #"Precomputed": "02_precomputed", 
            "Datasaurus": "03_datasaurus", 
            "Custom": "04_custom", 
            "About": "05_about"}
st.sidebar.header("Select page")
selected_page = st.sidebar.selectbox("Select page", page_dict.keys())
selected_module = page_dict[selected_page]

# Render the content
current_module = importlib.import_module(selected_module)
current_module.display_page()