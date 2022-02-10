import streamlit as st

from py_code import visualization
from py_code import generation

def display_page():
    # Set title
    st.title("Datasaurus")

    # Set header
    st.header("When data run the earth")
    st.markdown("Animation is computed on the fly")

    # The content
    c1, c2, c3 = st.columns([1, 1, 3])
    shape_start_options = ['dino', 'rando', 'slant', 'big_slant']
    shape_end_options = ['x', 'h_lines', 'v_lines', 'wide_lines', 'high_lines', 
                        'slant_up', 'slant_down', 'center', 'star', 'down_parab', 
                        'circle', 'bullseye', 'dots','streamlit']
    shape_start = c1.selectbox("Select the starting shape", shape_start_options)
    shape_end = c2.selectbox("Select the target shape", shape_end_options)

    df = generation.load_dataset(shape_start)
        
    if st.button("Run"):
        # Placeholders to be filled in later
        progress_bar_placeholder = st.empty()
        altair_placeholder = st.empty()
        num_frames = 1000
        for frame in range(num_frames):
            df = generation.run_pattern(df, shape_start, shape_end, iters=100, num_frames=1, decimals=2)
            progress = frame / num_frames
            visualization.animate_from_df(df, progress_bar_placeholder, altair_placeholder, progress, num_frames)