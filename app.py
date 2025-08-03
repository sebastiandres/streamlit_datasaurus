import streamlit as st
import os

# Set page configuration
st.set_page_config(
                        layout="wide", page_title="Datasaurus Rex",
                        page_icon="🦖",
                        initial_sidebar_state="expanded"
                )

# Configure the pages
#delete_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")
why = st.Page(os.path.join("docs", "00_why.py"), title="Welcome!")
intro = st.Page(os.path.join("docs", "01_intro.py"), title="What is a Datasaurus?")
datasaurus = st.Page(os.path.join("docs", "03_datasaurus.py"), title="Where can I see one?")
custom = st.Page(os.path.join("docs", "04_custom.py"), title="Can I create a Datasaurus?")
about = st.Page(os.path.join("docs", "05_about.py"), title="About")

pg = st.navigation([why, intro, datasaurus, custom, about], position="top")
pg.run()