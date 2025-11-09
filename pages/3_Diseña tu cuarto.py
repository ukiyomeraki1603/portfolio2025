import streamlit as st
col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/4.jpg", width=1500)

st.markdown(
    """
    <style>
   

    /* Sidebar marrón clarito y texto negro en Georgia */
    .stSidebar {
        background-color: #d8c3a5 !important; /* marrón clarito */
        font-family: 'Georgia', serif !important;
        color: #000000 !important; /* texto negro */
    }

    

    /* Mantener tipografía por defecto en pestañas de navegación de páginas */
    [data-testid="stHorizontalBlock"] {
        font-family: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.text("Esta actividad consistió de la creación, ideación y modelado de un espacio de descanso, uno de estudio y uno de ocio adaptado a las necesidades y gustos creativos de los participantes. En particular, elegí mezclar una estética de interior clásico con elementos de diseño japonés, como lo son las puertas corredizas (shōji). También elegí diseñar un jardín que acompañase la estética, fusionando elementos europeos con vegetación asiática. ")
st.text("El modelado y los planos fueron creados con SketchUp y posteriormente renderizados con Twinmotion.")
st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/shizuku1.jpg", width=1000)
st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/shizuku2.jpg", width=1000)

st.text("Por último, realicé un video recorriendo el modelo")

st.video("https://youtu.be/Mxh4zZG4xHM")

