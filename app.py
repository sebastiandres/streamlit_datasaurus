import streamlit as st
import streamlit_book as stb

# Set page configuration
st.set_page_config(layout="wide", page_title="Datasaurus Rex",
                   page_icon="🦖",
                   initial_sidebar_state="expanded")

# Streamit book properties
stb.set_book_config(menu_title="Datasaurus Rex",
                    menu_icon="info-square",
                    options=[
                            "Welcome!",
                            "What is a Datasaurus?",
                            "Where can I see one?",
                            "Can I create a Datasaurus?",
                            "About"
                            ],
                    paths=[
                            "docs/00_why.py",
                            "docs/01_intro.py",
                            "docs/03_datasaurus.py",
                            "docs/04_custom.py",
                            "docs/05_about.py"
                          ],
                    )
