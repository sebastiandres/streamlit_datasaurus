import streamlit as st

from py_code import visualization
from py_code import generation
from py_code import keywords

def display_page():
    # Set title
    st.title("Datasaurus")

    # Set header
    st.header("When data run the earth")
    st.markdown("Loading precomputed dataset from disk")

    # The content
    c1, c2, c3 = st.columns([1, 1, 3])
    shape_start_options = keywords.INITIAL_DATASETS
    shape_end_options = keywords.ALL_TARGETS
    shape_start = c1.selectbox("Select the starting shape", shape_start_options)
    shape_end = c2.selectbox("Select the target shape", shape_end_options)

    c3.markdown("")
    c3.markdown("")
    if c3.button("Show me!"):
        visualization.animate_from_path(shape_start, shape_end)
        