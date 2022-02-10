import streamlit as st

def display_page():
    # Set title
    st.title("About")

    # Authors
    st.header("The authors")
    st.markdown("""
    * Diego Rojo:\t\t[website](https://www.93degree.me/) - [github](https://github.com/93degree) - [linkedin](https://www.linkedin.com/in/diego-rojo/) - [twitter](https://twitter.com/Diego_Rojo_)
    * Sebastián Flores:\t\t[website](https://sebastiandres.github.io/blog/) - [github](https://github.com/sebastiandres) - [linkedin](https://www.linkedin.com/in/sebastiandres/) - [twitter](https://twitter.com/sebastiandres)""")

    # Anscombe
    st.header("The Anscombe Dataset")
    st.markdown("""
    * Lorem
    * Ipsum
    """)    


    # Datasaurius
    st.header("The Datasaurus")
    st.markdown("""
    * Lorem
    * Ipsum
    """)    

    # Other links and references
    st.header("Links and references")
    st.markdown("""
    * The gifs: made with [youtube](https://www.youtube.com/watch?v=h58lRIVHhGc) and [gifrun](https://gifrun.com/)
    """)