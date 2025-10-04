import streamlit as st

# ---------- ESTILOS UNIVERSALES ----------
st.markdown(
    """
    <style>
    /* Fondo blanco y tipografía Georgia forzada en contenido principal */
    .main .block-container {
        background-color: #ffffff !important;
        font-family: 'Georgia', serif !important;
        color: #000000 !important; /* texto negro */
    }

    /* Sidebar marrón clarito y texto negro en Georgia */
    .stSidebar {
        background-color: #d8c3a5 !important; /* marrón clarito */
        font-family: 'Georgia', serif !important;
        color: #000000 !important; /* texto negro */
    }

    /* Forzar texto negro en widgets de sidebar */
    .stSidebar .stTextInput input,
    .stSidebar .stTextArea textarea,
    .stSidebar .stSelectbox select,
    .stSidebar .stSlider>div>div>div>input,
    .stSidebar .stButton>button,
    .stSidebar label {
        color: #000000 !important;
        font-family: 'Georgia', serif !important;
    }

    /* Mantener tipografía por defecto en pestañas de navegación de páginas */
    [data-testid="stHorizontalBlock"] {
        font-family: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
