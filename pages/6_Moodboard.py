
import streamlit as st
from pathlib import Path # para manejar archivos e imagenes 

# diseño de la barra lateral

st.markdown(
    """
    <style>
    /* Sidebar marrón clarito y texto negro en Georgia */
    .stSidebar {
        background-color: #d8c3a5 !important;
        font-family: 'Georgia', serif !important;
        color: #000000 !important;
    }
    /* Mantener tipografía por defecto en pestañas de navegación de páginas */
    [data-testid="stHorizontalBlock"] {
        font-family: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("assets/mooodboard.png", width=1500)

ASSETS_DIR = Path("assets")


# session_state guarda valores en la sesión

def init_state():
    if "notas" not in st.session_state:
        st.session_state.notas = []
    if "current" not in st.session_state:
        st.session_state.current = {
            "nombre": "",
            "tipo": "Vivienda familiar",
            "estilos": [],
            "elementos": [],
            "tam_m2": 20,
        }
    if "moodboards" not in st.session_state:
        st.session_state.moodboards = []
    if "matched_auto" not in st.session_state:
        st.session_state.matched_auto = []

# Escaneo de imágenes

def scan_images():
    imgs = []
    if not ASSETS_DIR.exists():
        return imgs
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        imgs.extend(sorted(ASSETS_DIR.rglob(ext)))
    return imgs

# Diccionarios de imágenes 

tipo_images_map = {
    "Vivienda familiar": ["viviendafamiliar1.jpg", "viviendafamiliar22.jpg"],
    "Diseño interior": ["reciclado1.jpg", "reciclado2.jpg"],
    "Intervención urbana": ["urbano1.jpg", "urbano2.jpg"]
}

estilo_images_map = {
    "Minimalista": ["minimalista1.jpg", "minimalista2.jpg"],
    "Industrial": ["industrial1.jpg", "industrial2.jpg"],
    "Clásico": ["clasico1.jpg", "clasico2.jpg"],
    "Orgánico": ["organico1.jpg", "organico2.jpg"],
    "Vanguardista": ["vanguardista1.jpg", "vanguardista2.jpg"]
}

elemento_images_map = {
    "Iluminación natural": ["iluminación1.jpg","iluminación2.jpg"],
    "Materiales reciclados": ["panel1.jpg","panel2.jpg"],
    "Espacios multifuncionales": ["multifuncional1.jpg","multifuncional2.jpg"],
    "Jardín / Vegetación": ["planta1.jpg","planta2.jpg"],
}

# -------------------------
# Inicialización
# -------------------------
init_state()
all_images = scan_images()


# Página principal

st.write("Diseña tu propio moodboard con recomendaciones generales automáticamente")

# 1) Datos básicos
st.subheader(" Datos del proyecto")
col1, col2, col3 = st.columns([2,2,1])
with col1:
    nombre = st.text_input("Nombre del proyecto", value=st.session_state.current["nombre"])
with col2:
    tipo = st.selectbox("Tipo de proyecto", options=list(tipo_images_map.keys()),
                        index=list(tipo_images_map.keys()).index(st.session_state.current.get("tipo","Vivienda familiar")))
with col3:
    tam = st.slider("Tamaño estimado (m²)", 5, 200, value=st.session_state.current.get("tam_m2",20))

st.session_state.current.update({"nombre": nombre, "tipo": tipo, "tam_m2": tam})

# 2) Estilos
st.subheader(" Paleta conceptual y estilos")
estilos = st.multiselect("Seleccioná uno o más estilos", options=list(estilo_images_map.keys()),
                         default=st.session_state.current.get("estilos", []))
st.session_state.current["estilos"] = estilos

# Tips condicionales
for e in estilos:
    if e == "Industrial":
        st.info("Tip: combiná texturas rugosas (ladrillo, hormigón) con metales expuestos.")
    elif e == "Minimalista":
        st.info("Tip: priorizá espacios despejados y colores neutros.")

# 3) Elementos
st.subheader(" Elementos y prioridades")
elementos = st.multiselect("¿Qué elementos querés incluir?", options=list(elemento_images_map.keys()),
                           default=st.session_state.current.get("elementos", []))
st.session_state.current["elementos"] = elementos

if "Eficiencia energética" in elementos:
    st.write("Considerá paneles solares, orientación y buen aislamiento.")


# 4) Va generando automaticamente el moodboard (solo en sesión, no la muestra)



auto_matched = []

# Tipo
for img_name in tipo_images_map.get(tipo, []):
    p = ASSETS_DIR / img_name
    if p.exists() and p not in auto_matched:
        auto_matched.append(p)

# Estilos
for e in estilos:
    for img_name in estilo_images_map.get(e, []):
        p = ASSETS_DIR / img_name
        if p.exists() and p not in auto_matched:
            auto_matched.append(p)

# Elementos
for el in elementos:
    for img_name in elemento_images_map.get(el, []):
        p = ASSETS_DIR / img_name
        if p.exists() and p not in auto_matched:
            auto_matched.append(p)

st.session_state.matched_auto = [str(p) for p in auto_matched]

# No muestra las imágenes todavía


#prepara el block de notas

st.subheader(" Bloc de notas creativo")
nota_text = st.text_area("Escribí una idea, referencia o comentario", height=120)
colb1, colb2 = st.columns([1,1])
with colb1:
    if st.button("Guardar nota"):
        if nota_text.strip():
            st.session_state.notas.append(nota_text.strip())
            st.success("Nota guardada")
        else:
            st.warning("La nota está vacía")
with colb2:
    if st.button("Borrar todas las notas"):
        st.session_state.notas = []
        st.info("Se borraron las notas de la sesión")

if st.session_state.notas:
    st.write("**Tus notas:**")
    for i, n in enumerate(st.session_state.notas, 1):
        st.markdown(f"**{i}.** {n}")

# -------------------------
# 8) Guardar / Exportar + Póster final
# -------------------------
st.markdown("---")
st.subheader(" Guardar / Exportar")

if st.button("Guardar moodboard en la sesión"):
    mb = {
        "nombre": st.session_state.current["nombre"],
        "tipo": st.session_state.current["tipo"],
        "tam_m2": st.session_state.current["tam_m2"],
        "estilos": st.session_state.current["estilos"],
        "elementos": st.session_state.current["elementos"],
        "notas": list(st.session_state.notas),
        "imagenes": [Path(p).name for p in st.session_state.matched_auto],
    }
    st.session_state.moodboards.append(mb)
    st.success(" Moodboard guardado correctamente en la sesión.")

    # Mostrar póster  final

    st.markdown("---")
    st.markdown("##  Póster final del proyecto")
    st.markdown(
        f"""
        <div style='font-size:22px; font-weight:bold; margin-bottom:10px;'>{mb['nombre']}</div>
        <div style='font-size:18px; margin-bottom:5px;'> Tipo: <b>{mb['tipo']}</b></div>
        <div style='font-size:18px; margin-bottom:5px;'> Tamaño: <b>{mb['tam_m2']} m²</b></div>
        <div style='font-size:18px; margin-bottom:5px;'> Estilos: <b>{', '.join(mb['estilos']) if mb['estilos'] else '—'}</b></div>
        <div style='font-size:18px; margin-bottom:5px;'> Elementos: <b>{', '.join(mb['elementos']) if mb['elementos'] else '—'}</b></div>
        """,
        unsafe_allow_html=True
    )

    if mb["notas"]:
        st.markdown("###  Notas creativas")
        for i, n in enumerate(mb["notas"], 1):
            st.markdown(f"- {n}")

    if mb["imagenes"]:
        st.markdown("###  Moodboard visual")
        cols = st.columns(3)
        for i, img_name in enumerate(mb["imagenes"]):
            img_path = ASSETS_DIR / img_name
            if img_path.exists():
                with cols[i % 3]:
                    st.image(str(img_path), caption=img_name, use_container_width=True)
    else:
        st.info("No se encontraron imágenes asociadas al moodboard.")
