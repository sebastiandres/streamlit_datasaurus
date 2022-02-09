import streamlit as st
from py_code import datasaurus

def display_page():
    # Set title
    st.title("Datasaurus")

    # Set header
    st.header("When data run the earth")

    # The content
    c1, c2 = st.columns(2)
    shape_start_options = ['dino', 'rando', 'slant', 'big_slant']
    shape_end_options = ['x', 'h_lines', 'v_lines', 'wide_lines', 'high_lines', 'slant_up', 'slant_down', 'center', 'star', 'down_parab', 'circle', 'bullseye', 'dots']
    shape_start = c1.selectbox("Select the starting shape", shape_start_options)
    shape_end = c2.selectbox("Select the target shape", shape_end_options)

    if st.button("Run"):
        datasaurus.run(shape_start, shape_end)