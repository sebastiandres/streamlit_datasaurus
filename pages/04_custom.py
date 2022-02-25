import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

from py_code import visualization
from py_code import generation
from py_code import keywords

def clear_lines():
    st.session_state["lines"] = []

# Set title
st.title("Can I have my own Datasaurus?")
st.markdown("YES. YOU CAN CREATE YOUR OWN DATASAURUS!!! HOW CRAZY IS THAT???!!! \n\n Define the number of random points and the figure, and explore how the points converge!")

## Input
c1, c2 = st.columns([4, 6])
c1.header("Input")
c1.markdown("Select the number of random points between 0 and 100 with the slider below")
num_points = c1.slider("Number of points", min_value=100, max_value=250, value=150, step=10)
points = np.random.uniform(low=[0,0], high=[100,100], size=(num_points,2))
df = pd.DataFrame(data=points, columns=["x", "y"])
c2.altair_chart(visualization.scatterplot_from_df(df))

# The content
st.header("Target")
shape_start = "rando"
shape_end = "drawable_canvas"
c1, c2, c3, c4, c5 = st.columns([1,1,1,2,1])
x1 = c1.number_input("Line start: x1", min_value=0,  max_value=100, value=20)
y1 = c2.number_input("Line start: y1", min_value=0,  max_value=100, value=20)
x2 = c1.number_input("Line end: x2", min_value=0,  max_value=100, value=80)
y2 = c2.number_input("Line end: y2", min_value=0,  max_value=100, value=80)

# Start with the streamlit shape
if "lines" not in st.session_state:
    l1 = [[18.75, 20], [0, 65]]
    l2 = [l1[-1], [31.25, 49.375]]
    l3 = [l2[-1], [50, 73.125]]
    l4 = [l3[-1], [68.75, 49.375]]
    l5 = [l4[-1], [100, 64]]
    l6 = [l5[-1], [81.25, 20]]
    l7 = [l6[-1], l1[0]]
    lines = [l1, l2, l3, l4, l5, l6, l7]
    st.session_state["lines"] = lines
    
if c3.button("Add Line"):
    st.session_state["lines"].append([[x1,y1], [x2,y2]])

# Draw current lines
c4.altair_chart(visualization.chart_from_lines(st.session_state["lines"]))
c5.button("Clear Lines", on_click=clear_lines)

# The Iteration
st.title("Iteration")
c1, c2 = st.columns([1, 9])
if len(st.session_state["lines"])==0:
    st.markdown("Please add at least 1 line")
else:
    run = c1.button("Run")
    c2.markdown("Simulation can take up to 5 minutes. Please be patient.")
    if run:
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