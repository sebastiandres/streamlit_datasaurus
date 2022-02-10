import streamlit as st

def display_page():

    c1, c2 = st.columns([4,6])
    image_placeholder = c1.empty()
    markdown_placeholder = c2.empty()
    button_placeholder = c2.empty()

    # Markdown for image
    image_markdown_format = "![Alt Text](https://github.com/sebastiandres/streamlit_datasaurus/blob/main/images/{}?raw=true)"

    # Content
    image_placeholder.markdown(image_markdown_format.format("mrdna1.gif"))
    markdown_placeholder.markdown("""    
    Data Science and Jurassic Park are very similar:
    """)

    if button_placeholder.button("Why?"):
        #image_placeholder.images("images/mrdna2.gif", width=300)
        image_placeholder.markdown(image_markdown_format.format("mrdna2.gif"))
        markdown_placeholder.markdown("""
        Data Science and Jurassic Park are very similar:
        * You have to ponder the meaning of life
        * You have to consider not only if you can, but also if you should.
        * It always seems to work great until your first real customer. 
        * You have to dig for the relevant data and fix it with the most unusual ways. It might look ok but mayhem can (and will) arise later.
        * Your creations will likely bite you back (?).
        * It was all good until lawyers and business man started making decisions.
        """)
        button_placeholder.empty()
        st.markdown("Use the sidebar to go through this interactive Streamlit app to learn about the ellusive Datasaurus.")
