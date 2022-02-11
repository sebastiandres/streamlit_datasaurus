import streamlit as st

from py_code import visualization

def display_page():

    # Set title
    st.title("What is a Datasaurus?")

    st.markdown("""
    A Datasaurus is a constant remainder that you must always, always, always plot your data. 
    The statistics are not enough.
    """)

    st.markdown("""
    12 different datasets have the same statistics up to the second decimal: 
    * Average x: 54.26
    * Average y: 47.83
    * Standard Deviation x: 16.76
    * Standard Deviation x: 26.93
    * Pearson's Correlation: -0.06
    """)

    c1, c2, c3, c4 = st.columns([2,1,2,1])
    radio_options = ("Not much, almost the same.", "They can be different.")
    answer = c1.radio("How different you think the datasets can be?", 
                        radio_options, index=0)
    c2.markdown("\n") # To make the button move down
    c2.markdown("\n") # To make the button move down
    if "answered" not in st.session_state:
        st.session_state["answered"] = False
    if c2.button("Check answer") or st.session_state["answered"]:
        st.session_state["answered"] = True
        c3.markdown("\n") # To make the button move down
        c3.markdown("\n") # To make the button move down
        if answer == radio_options[0]:
            c3.markdown("HA! Sweet innocence. They can be VERY different.")
        else:
            c3.markdown("True. They can be VERY different.")

    # Put a reveal button
    if st.session_state["answered"] and c2.button("Plot the Data!!!"):
        visualization.plot_datasaurus_sets()

    '''
    # DIEGO, ACÁ CREO QUE PODRÍAS COMPLETAR ESTO!
    with st.expander("Historical notes"):
        # Content
        st.markdown("""
        Describe:
        - Anscombe's paper
        - Datasaurius
        - How presenting the data in a interactive way was the natural step
        """)
    '''
