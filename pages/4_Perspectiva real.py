import streamlit as st
col1, col2, col3 = st.columns([1,2,1])  
with col2:
    st.image("assets/5.jpg", width=1500)
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


st.markdown("""
La perspectiva real es un sistema gráfico utilizado en dibujo técnico para representar objetos tridimensionales sobre un plano de manera proporcionada y coherente con la visión humana, mediante un procedimiento geométrico y metódico.
""")



# Bibliografía en un desplegable
with st.expander("Fuentes bibliográficas"):
    st.markdown("""
     Ching, F. D. K. (2015). *Architectural Graphics*. Hoboken: Wiley.  
     Piña, M. (2012). *Dibujo Arquitectónico: Técnicas y Perspectiva*. Barcelona: Gustavo Gili.  
     Ballesteros, J. (2009). *Perspectiva y representación arquitectónica*. Madrid: Editorial Paraninfo.  
     Curl, J. S. (2006). *A Dictionary of Architecture and Landscape Architecture* (2nd ed.). Oxford: Oxford University Press.  
     Fröhlich, H. (2008). *Perspectiva y geometría aplicada al dibujo arquitectónico*. Buenos Aires: Ediciones Infinito.
    """)










col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Procedimiento de las intersecciones mediante una direccion natural y los planos visuales

    """)
    st.markdown("""
Al representar objetos complejos en perspectiva real, a menudo es necesario determinar las intersecciones entre elementos (como techos, columnas o volúmenes).  
Para ello se utiliza el procedimiento de intersecciones mediante una dirección natural, apoyado en planos visuales que ayudan a trasladar medidas con precisión.
""")

st.header("Conceptos clave")
st.markdown("""
- **Dirección natural:** Línea elegida para proyectar los vértices y bordes de los objetos de manera más sencilla, generalmente perpendicular o paralela a los elementos a intersectar.  
- **Planos visuales:** Planos auxiliares que permiten ubicar los puntos de intersección entre elementos y trasladarlos correctamente a la perspectiva real.
""")

# Procedimiento
st.header("Procedimiento")
st.markdown("""
1. Identificar los elementos que se intersectan.  
2. Elegir una dirección natural para facilitar la proyección.  
3. Trazar planos visuales auxiliares pasando por los vértices o líneas importantes.  
4. Marcar los puntos de intersección en el plano visual y trasladarlos a la perspectiva mediante prolongaciones hacia los puntos de fuga.  
5. Unir los puntos resultantes para representar la intersección en la perspectiva.
""")
with col2:
    st.image("assets/real1.jpeg", width=500)

# ----- Segunda fila: imagen izquierda, texto derecha -----
col1, col2 = st.columns(2)
with col1:
    st.image("assets/real2.jpeg", width=500)
with col2:
    st.markdown("""
    ### Procedimiento de las prolongaciones
   
El procedimiento de las prolongaciones es una técnica utilizada para trasladar medidas y puntos desde las vistas ortogonales (planta, alzado o perfil) hacia la perspectiva real, manteniendo la proporción, escala y profundidad correctas.
""")

# Conceptos clave
st.header("Conceptos clave")
st.markdown("""
- **Prolongaciones:** Líneas auxiliares trazadas desde los vértices del objeto hacia el plano de perspectiva para ubicar los puntos en la vista en perspectiva.  
- **Puntos de fuga:** Las prolongaciones se dirigen hacia los puntos de fuga sobre la línea de horizonte, garantizando la sensación de profundidad.  
- **Líneas de referencia:** Ayudan a trasladar medidas y ubicar correctamente alturas, anchos y profundidades, respetando la proporción real.
""")

# Procedimiento paso a paso
st.header("Procedimiento")
st.markdown("""
1. Identificar los vértices del objeto en las vistas ortogonales (planta y alzado).  
2. Trazar líneas de prolongación desde cada vértice hacia los puntos de fuga correspondientes.  
3. Establecer líneas de referencia horizontales o verticales según corresponda, para ubicar alturas y profundidades.  
4. Marcar la posición de los vértices en el plano de perspectiva donde se cruzan las prolongaciones con las líneas de referencia.  
5. Unir los puntos resultantes para construir la figura completa en perspectiva real.  
6. Revisar que las proporciones y la convergencia de líneas sean coherentes, ajustando si es necesario.
""")

# ----- Tercera fila: texto izquierda, imagen derecha -----
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Procedimiento de los planos visuales
Los planos visuales son herramientas fundamentales para proyectar correctamente los puntos, líneas y superficies de un objeto desde las vistas ortogonales (planta y alzado) hacia la perspectiva real.  
Un plano visual es una superficie imaginaria que se coloca entre el observador y el objeto, y sirve para determinar cómo se verá cada punto del objeto en la representación en perspectiva.
""")

# Conceptos clave
st.header("Conceptos clave")
st.markdown("""
- **Plano Visual Vertical (PVV):** Plano que se coloca frente al observador, perpendicular a la línea de horizonte. Sobre él se proyectan los puntos para definir la profundidad.  
- **Plano Visual Horizontal (PVH):** Plano que pasa por la línea de horizonte y se usa para ubicar alturas o niveles de los puntos del objeto.  
- **Puntos de intersección:** Son los puntos donde las líneas de proyección cortan los planos visuales; definen la forma del objeto en perspectiva.
""")

# Procedimiento paso a paso
st.header("Procedimiento")
st.markdown("""
1. Identificar las vistas ortogonales del objeto (planta, alzado o perfil).  
2. Trazar los planos visuales según las direcciones principales (vertical y horizontal).  
3. Proyectar los puntos del objeto desde las vistas ortogonales hacia los planos visuales mediante líneas perpendiculares.  
4. Determinar los puntos de intersección entre las proyecciones y los planos visuales.  
5. Trasladar esos puntos al plano de perspectiva utilizando prolongaciones hacia los puntos de fuga.  
6. Unir los puntos obtenidos para formar las líneas y caras del objeto en la perspectiva real.
""")

with col2:
    st.image("assets/real3.jpeg", width=500)


st.image("assets/real4.jpeg", width=1000)


st.image("assets/real5.jpeg", width=1000)

st.image("assets/real6.jpeg", width=1000)


