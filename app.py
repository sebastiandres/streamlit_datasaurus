import streamlit as st
import streamlit_book as stb

# Set page configuration
st.set_page_config(layout="wide", page_title="Streamlitsaurus Rex",
                   page_icon="🦖",
                   initial_sidebar_state="expanded")

# Streamit book properties
stb.set_book_config(menu_title="Streamlitsaurus Rex",
                    menu_icon="",
                    options=[
                            "Welcome!",
                            "What is a Datasaurus?",
                            "Where can I see one?",
                            "Can I create a Datasaurus?",
                            "About"
                            ],
                    paths=[
                            "pages/00_why.py",
                            "pages/01_intro.py",
                            "pages/03_datasaurus.py",
                            "pages/04_custom.py",
                            "pages/05_about.py"
                          ],
                    )
