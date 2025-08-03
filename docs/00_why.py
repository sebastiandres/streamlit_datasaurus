import streamlit as st

def display_page():
    st.title("Welcome!")
    c2, c1 = st.columns(2)
    image_placeholder = c1.empty()

    # Markdown for image
    image_markdown_format = "![Alt Text](https://github.com/sebastiandres/streamlit_datasaurus/blob/main/images/{}?raw=true)"

    # Content
    image_placeholder.markdown(image_markdown_format.format("mrdna1.gif"))
    c2.markdown("""    
    Why are **Jurassic Park** and **Data Science** are similar?
    """)

    button_placeholder = c2.empty()

    if button_placeholder.button("Why?"):
        image_placeholder.markdown(image_markdown_format.format("mrdna2.gif"))
        c2.markdown("""
        * Scientists are so preoccupied with whether they can, they don't stop to think if they should.
        * Everything seems to work _until_ your first real customer. 
        * Filling gaps in your data might look ok but will lead to problems!
        * Your creations will likely bite you back (?).
        * It was all good until lawyers and business man started making decisions.
        """)
        button_placeholder.empty()

        c1, c2, c3 = st.columns([1,2,1])

        c2.markdown("Join the quest to learn about the ellusive Datasaurus.")

        c2.markdown("Use the top bar to navigate through this interactive Streamlit app")

display_page()