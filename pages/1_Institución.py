import streamlit as st

# ---------- ESTILOS UNIVERSALES ----------
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


col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/2.jpg", width=1500)

st.text( "La primera actividad del año fue en grupos, y consistió en la evaluación de un espacio de la institución educativa, su registro y reación de un elemento arquitectónico partiendo de la planta base. ")





col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Primera fase
    Registramos el entorno en el cual nos íbamos a basar y realizamos un croquis libre del mismo. Utilicé como recurso la línea y mancha, aplicando la técnica de acuarela y tinta sobre papel blanco.
    """)
    
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-4.jpeg", width=500)


col1, col2 = st.columns(2)
with col1:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-1.jpeg", width=500)
with col2:
    st.markdown("""
    Una vez seleccionada el área de estudio, realizamos un registro de su planta con medidas.
    """)
   

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    Realizamos un croquis del plano a escala. Utilicé como recurso la línea y apliqué la técnica de tinta sobre papel blanco.
    """)
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-2.jpeg", width=500)


col1, col2 = st.columns(2)
with col1:
   st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-3.jpeg", width=500)
with col2:
    
     st.markdown("""
    Posteriormente, un corte de planta. Elegí aplicar mancha de marcadores y línea de fibras sobre papel blanco.
    Opté por una paleta de tonos azules.
    """)


col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Fase 2
    Comenzamos la ideación de un elemento arquitectónico basándonos en la planta anteriormente estudiada. Este es uno de los croquis de ideación, donde se muestra al objeto visto en perspectiva a dos puntos de fuga.
    """)
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-5.jpeg", width=500)


col1, col2 = st.columns(2)
with col1:
      st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-6.jpeg", width=500)
with col2:
    st.markdown("""
    Aquí apreciamos sotro croquis con más detalle, reaizado en papel blanco, recurso línea y técnica fibra negra.
    """)

col1, col2 = st.columns(2)
with col1:
     st.markdown("""
    Se representó la casa en perspectiva isométrica. (Debo aclarar que no disfruté el proceso de las veinticinco elipses en perspectiva).
    """)
with col2:
   
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-7.jpeg", width=500)


col1, col2 = st.columns(2)
with col1:
   st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1-8.jpeg", width=500)
with col2:
    st.markdown("""
   Una vez realizado el modelo 3D, renderizamos el modelo con Gendo Ai.
    """)

   
st.markdown(
    """
    ## Conclusiones  
    Para finalizar el proceso, creamos un póster digital.
    """
)

col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/proy1poster.jpeg")



