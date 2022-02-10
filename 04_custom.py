import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

from py_code import visualization
from py_code import generation

def display_page():
    # Set title
    st.title("Draw-your-adventure")
    st.markdown("Here you can draw a figure by segments and attempt to converge to it!")

    ## Input
    # Lines from canvas
    st.header("Input")
    c1, c2 = st.columns([4, 6])
    num_points = c1.slider("Number of points", min_value=100, max_value=250, value=150, step=10)
    points = np.random.uniform(low=[0,0], high=[100,100], size=(num_points,2))
    df = pd.DataFrame(data=points, columns=["x", "y"])
    rando_plot = (alt.Chart(df)
                    .mark_circle()
                    .encode(
                        alt.X("x", scale=alt.Scale(domain=(0, 100))),
                        alt.Y("y", scale=alt.Scale(domain=(0, 100))),
                    ))
    c2.altair_chart(rando_plot)

    # The content
    st.header("Target")
    st.markdown("The initial shape will be random points to obtain better results")
    shape_start = "rando"

    st.markdown("Draw lines on desired end shape, with the convention Line Start (x1,y1) -> Line End (x2,y2)")
    shape_end = "drawable_canvas"
    c1, c2, c3, c4, c5 = st.columns([1,1,1,2,1])
    x1 = c1.number_input("Line start: x1", min_value=0,  max_value=100, value=0)
    y1 = c2.number_input("Line start: y1", min_value=0,  max_value=100, value=0)
    x2 = c1.number_input("Line end: x2", min_value=0,  max_value=100, value=100)
    y2 = c2.number_input("Line end: y2", min_value=0,  max_value=100, value=100)

    if "lines" not in st.session_state:
        st.session_state["lines"] = []

    if c3.button("Add Line"):
        st.session_state["lines"].append([[x1,y1], [x2,y2]])
    
    # Draw current lines
    plot = alt.LayerChart() # Starting value, empty chart
    for line in st.session_state["lines"]:
        df_lines = pd.DataFrame(data=line, columns=["x", "y"])
        plot = plot + alt.Chart(df_lines).mark_line().encode(x='x',y='y')
    c4.altair_chart(plot)
    if c5.button("Clear Lines"):
        st.session_state["lines"] = []


    st.title("Iteration")
    if len(st.session_state["lines"])==0:
        st.markdown("Please add at least 1 line")
    elif st.button("Run"):
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