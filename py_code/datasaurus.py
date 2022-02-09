# Wrapper for the online code
import streamlit as st
import time 

def run(shape_start, shape_end):
    ph1 = st.empty()
    ph2 = st.empty()
    for i in range(101):
        time.sleep(0.01)
        ph1.write(shape_start+" -> "+shape_end)
        ph2.progress(i)
    ph2.empty()