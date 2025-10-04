
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

    /* Banner superior estilo art déco */
    .banner {
        background: linear-gradient(135deg, #d8c3a5, #c2b280);
        padding: 50px;
        text-align: center;
        border-bottom: 6px solid #8a6f48;
        letter-spacing: 4px;
        font-size: 4rem;
        font-weight: bold;
        color: #ffffff;
        text-transform: uppercase;
        text-shadow: 2px 2px #5a4635;
        border-radius: 0px 0px 15px 15px;
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

    <style>
    /* Forzar fondo blanco y tipografía solo en contenido principal */
    .main .block-container {
        background-color: #ffffff !important;
        font-family: 'Georgia', serif !important;
        color: #3b2f2f !important;
        padding-top: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENIDO ----------
# Banner principal
st.markdown("<div class='banner'>Presentación</div>", unsafe_allow_html=True)

# Panel de texto (editable)
with st.container():
    st.markdown(
        """
        <div class='panel'>
            <h2>Título de tu presentación</h2>
            <p>
                Escribí aquí tu presentación. Podés contar quién sos, cuál es tu estilo artístico,
                qué representa tu trabajo, o cualquier mensaje que quieras compartir con quienes visiten tu portfolio.
                Este texto es completamente editable.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

