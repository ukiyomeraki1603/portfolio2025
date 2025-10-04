import streamlit as st

# Lista de páginas: cada página es un diccionario con imagen y texto
paginas = [
    {"imagen": "assets/croquis_1.jpg", "texto": "Primera página del libro"},
    {"imagen": "assets/croquis_2.jpg", "texto": "Segunda página del libro"},
    {"imagen": "assets/croquis_3.jpg", "texto": "Tercera página del libro"}
]

# Inicializar página actual
if "pagina" not in st.session_state:
    st.session_state["pagina"] = 0

# Botones de navegación
col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.button("◀ Anterior") and st.session_state["pagina"] > 0:
        st.session_state["pagina"] -= 1
with col3:
    if st.button("Siguiente ▶") and st.session_state["pagina"] < len(paginas)-1:
        st.session_state["pagina"] += 1

# Mostrar contenido de la página actual
pagina_actual = st.session_state["pagina"]
st.image(paginas[pagina_actual]["imagen"], use_column_width=True)
st.markdown(f"**{paginas[pagina_actual]['texto']}**")


st.markdown(
    """
    <style>
    /* Fondo y tipografía */
    html, body, .main, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background-color: #faf9f6 !important; /* fondo blanco tipo cottagecore */
        color: #3b2f2f !important;
        font-family: 'Georgia', serif;
    }

    /* Marco de la "página" del libro */
    .book-page {
        background-color: #ffffff;
        border: 3px solid #c2b280; /* borde art deco */
        border-radius: 15px;
        padding: 20px;
        margin: 30px auto;
        max-width: 700px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    /* Imagen dentro de la página */
    .book-page img {
        max-width: 80%;   /* imágenes más pequeñas */
        height: auto;
        display: block;
        margin: 0 auto 15px auto;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Texto dentro de la página */
    .book-page p {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: center;
        color: #3b2f2f;
    }

    /* Botones de navegación */
    .stButton>button {
        background-color: #d8c3a5;
        color: #3b2f2f;
        border-radius: 12px;
        padding: 8px 16px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #c2b280;
        color: #ffffff;
    }
    
    <style>
    /* Forzar fondo blanco y tipografía solo en contenido principal */
    .main .block-container {
        background-color: #ffffff !important;
        font-family: 'Georgia', serif !important;
        color: #3b2f2f !important;
        padding-top: 0px;
    }

    /* Sidebar: color marrón clarito y tipografía Georgia */
    .stSidebar {
        background-color: #d8c3a5 !important;
        font-family: 'Georgia', serif !important;
        color: #3b2f2f !important;
    }

    /* Mantener tipografía por defecto en tabs de navegación de páginas */
    [data-testid="stHorizontalBlock"] {
        font-family: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)