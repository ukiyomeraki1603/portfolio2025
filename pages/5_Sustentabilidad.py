import streamlit as st
col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("assets/6.jpg", width=1500)
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

st.header("Propuesta")
st.text("Este proyecto se basó en la realización de una vivienda unifamiliar que incorporara méodos sustentables de construcción y aprovechase los recursos del lugar.")
st.text("Ideamos un entrepiso con una oficina estilo pecera para la madre, una biblioteca en el pasillo superior para la hija, y una huerta para el padre, que también es agricultor en el campo. Para aprovechar la mayor cantidad de espacio, destinamos el lugar de la mascota debajo de la escalera de la oficina de la madre.")
st.text("La disposición de ventanas aseguran tanto una unión con el resto de la casa (como lo es el de la cocina y los cuartos), como con la unión con la naturaleza.")
st.text("    ")



st.image("assets/lucernaposter.png", width=1500)

st.text("Realizamos una maqueta de estudio con cartón sueco, acetato, y nuestro querido amigo UHU. Su escala es 1:50 y mide 9cm de alto, con una planta de 18cm por 11cm.")

with open("assets.vid/maqueta.mp4", "rb") as video_file:
    st.video(video_file.read())

st.text("Dado que contábamos con un vasto terreno, decidimos agregar no solo un parrillero y cochera, sino una huerta y jardín organizado pensado para la sustentabilidad y para recibir visitas.")
st.text("También creamos un video renderizando el modelado de SketchUp en Twinmotion.")

with open("assets.vid/sust.mp4", "rb") as video_file:
    st.video(video_file.read())

st.text("Para más detalles, descargue la memoria descriptiva del proyecto:")
with open("assetspdf/memoria2025.pdf", "rb") as f:
    st.download_button(
        label="Descargar PDF",
        data=f,
        file_name="memoria2025.pdf",  
        mime="application/pdf"
    )
