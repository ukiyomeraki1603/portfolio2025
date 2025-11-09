import streamlit as st

# Imagen de portada centrada
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/3.jpg", width=1500)

st.text("En paralelo, se nos pidió que a lo largo de la primera mitad del año, realizaramos croquis de diferente estilo, para entregarlos en formato de libro. Yo elegí una encuadernación japonesa y forré las tapas utilizando la técnica de Decoupage.")
st.text("Presione los botones para pasar página del libro de croquis.")

# Lista de imágenes
paginas = [
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_1.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_2.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_3.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_4.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_5.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_6.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_7.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_8.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_9.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_10.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_11.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_12.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_13.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_14.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_15.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_16.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_17.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_18.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_19.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_20.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_21.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_22.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_23.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_24.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_25.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_26.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_27.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_28.jpg",
    "https://raw.githubusercontent.com/ukiyomeraki1603/portfolio2025/refs/heads/main/docs/assets/croquis_29.jpg"
]

# Inicializar página actual
if "pagina" not in st.session_state:
    st.session_state["pagina"] = 0

# Botones de navegación
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("◀ Anterior") and st.session_state["pagina"] > 0:
        st.session_state["pagina"] -= 1
with col3:
    if st.button("Siguiente ▶") and st.session_state["pagina"] < len(paginas) - 1:
        st.session_state["pagina"] += 1

# Mostrar la imagen actual centrada
pagina_actual = st.session_state["pagina"]
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        paginas[pagina_actual],
        width=400,
        use_container_width=False
    )

# Estilos CSS generales
st.markdown(
    """
    <style>
    html, body, .main, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background-color: #faf9f6 !important;
        color: #3b2f2f !important;
        font-family: 'Georgia', serif;
    }

    /* Botones */
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

    /* Fondo del contenido */
    .main .block-container {
        background-color: #ffffff !important;
        font-family: 'Georgia', serif !important;
        color: #3b2f2f !important;
        padding-top: 0px;
    }

    /* Sidebar */
    .stSidebar {
        background-color: #d8c3a5 !important;
        font-family: 'Georgia', serif !important;
        color: #3b2f2f !important;
    }

    [data-testid="stHorizontalBlock"] {
        font-family: inherit !important;
    }

    /* 🟤 Marco decorativo alrededor de las imágenes */
    .element-container img {
        border: 12px solid #b08b63; /* marrón cálido */
        border-radius: 15px;
        background-color: #fdfaf6;
        padding: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

