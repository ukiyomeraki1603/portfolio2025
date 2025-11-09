
import streamlit as st

# Configuración general de la página
st.set_page_config(page_title="Presentación", layout="wide")

# ---------- ESTILOS ----------
st.markdown(
    """
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

   

    /* Panel de presentación */
    .panel {
        background: #ffffff;
        padding: 50px;
        margin: 60px auto;
        max-width: 900px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border: 3px solid #c2b280;
    }

    .panel h2 {
        font-size: 2.5rem;
        color: #5a4635;
        margin-bottom: 20px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .panel p {
        font-size: 1.2rem;
        line-height: 1.8;
        text-align: justify;
        color: #3b2f2f;
    }

    
    """,
    unsafe_allow_html=True
)

# ---------- CONTENIDO ----------

# Panel de texto (editable)
# Imagen arriba del panel con tamaño más pequeño

col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("assets/1.jpg", width=1500)


with st.container():
    st.markdown(
        """
        <div class='panel'>
            <h2>Portfolio digital 2025</h2>
            <p>
                En este lugar expondré todos los trabajos realizados durante el curso de Comunicación Visual y Diseño dado para Sexto de Arquitectura, CTA.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


import streamlit as st

st.markdown(
    """
    <style>
    /* Aplica SOLO al contenido principal, no a la sidebar */
    .main {
        font-family: 'Georgia', serif !important;
        font-size: 20px !important;
        color: #000000 !important;
    }

    .main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
        font-family: 'Georgia', serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
