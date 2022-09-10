import streamlit as st

from py_code import visualization
from py_code import generation

from py_code import keywords

# Set title
st.title("Where can I see a Datasaurus?")

# Radio buttons with the options
options = {
            "This is important enough. I'll make some time. Compute and animate from scratch (slow, 2-3 minutes).":"compute",
            "I'm too important and have no time. Animate from precomputed values (fastest).":"animate",
            }
selected_option_text = st.radio("How much time can you spare?", options.keys(), index=0)
selected_option = options[selected_option_text]
if selected_option == list(options.values())[0]:
    # First option selected: compute slowly
    button_text = "Compute and Show!"
else:
    # Second options selected: just animate
    button_text = "SHOW ME, FAST!"

# The content
c1, c2, c3 = st.columns([1, 1, 3])
shape_start_options = keywords.INITIAL_DATASETS
shape_end_options = keywords.ALL_TARGETS
shape_start = c1.selectbox("Select the starting shape", shape_start_options)
shape_end = c2.selectbox("Select the target shape", shape_end_options)

c3.markdown("\n") # To make the button move down
c3.markdown("\n") # To make the button move down
if c3.button(button_text):
    if selected_option == "animate":
        visualization.animate_from_path(shape_start, shape_end)
    else:
        df = generation.load_dataset(shape_start)
        # Placeholders to be filled in later
        progress_bar_placeholder = st.empty()
        altair_placeholder = st.empty()
        num_frames = 1000
        for frame in range(num_frames):
            df = generation.run_pattern(df, shape_start, shape_end, iters=100, num_frames=1, decimals=2)
            progress = frame / num_frames
            visualization.animate_from_df(df, progress_bar_placeholder, altair_placeholder, progress, num_frames)
