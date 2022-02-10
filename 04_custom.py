import streamlit as st
import pandas as pd
import altair as alt

from py_code import visualization
from py_code import generation

def display_page():
    # Set title
    st.title("Draw-your-adventure")

    # Set header
    st.header("When data run the earth")

    # The content
    st.markdown("The initial shape will be random points to obtain better results")
    shape_start = "rando"

    st.markdown("Draw lines on desired end shape, with the convention Line Start (x1,y1) -> Line End (x2,y2)")
    shape_end = "drawable_canvas"
    c1, c2, c3, c4, c5, c6, c7 = st.columns([1,1,1,1,1,1,1])
    x1 = c2.number_input("x1", min_value=0,  max_value=100, value=0)
    y1 = c3.number_input("y1", min_value=0,  max_value=100, value=0)
    x2 = c5.number_input("x2", min_value=0,  max_value=100, value=100)
    y2 = c6.number_input("y2", min_value=0,  max_value=100, value=100)

    if "lines" not in st.session_state:
        st.session_state["lines"] = []

    if c7.button("Add Line"):
        st.session_state["lines"].append([[x1,y1], [x2,y2]])

    # Draw current lines
    plot = alt.LayerChart() # Starting value, empty chart
    for line in st.session_state["lines"]:
        df_lines = pd.DataFrame(data=line, columns=["x", "y"])
        plot = plot + alt.Chart(df_lines).mark_line().encode(x='x',y='y')
    st.altair_chart(plot)

    # Lines from canvas
    df = generation.load_dataset("rando")

    if st.button("Run"):
        # Get the lines
        lines_from_canvas = st.session_state["lines"]
        # Placeholders to be filled in later
        progress_bar_placeholder = st.empty()
        altair_placeholder = st.empty()
        num_frames = 1000
        for frame in range(num_frames):
            df = generation.run_pattern(df, shape_start, shape_end, 
                    lines_from_canvas=lines_from_canvas, iters=100, num_frames=1, decimals=2)
            progress = frame / num_frames
            visualization.animate_from_df(df, progress_bar_placeholder, altair_placeholder, progress, num_frames)