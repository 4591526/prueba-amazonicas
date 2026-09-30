import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import random
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Amazonicas",
    page_icon="🌿",
    layout="wide"
)

col1, col2, col3 = st.columns([1,3,1], gap="small")
with col2:
    st.image("logo_amazonicas.png", width=1500)
    st.image("banner_amazonicas.png", width=1800)
        
#st.markdown(f'<h1 style="font-size: 60px; text-align: center; color: green">Amazonicas XI</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Selectbox */
    div[data-baseweb="select"] > div {
        color: black !important;
        background-color: white !important;
        border: 1px solid #555 !important;
    }

    /* Opciones desplegables */
    div[role="option"] {
        color: black !important;
        background-color: white !important;
    }

    /* Texto dentro del select */
    div[data-baseweb="select"] span {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

idioma = st.selectbox(
    "",
    ["Español", "English", "Português"],
    label_visibility="collapsed"
)

menus = { "Español": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programación", "Organizadores": "Organizadores", 
                      "Convocatoria": "Convocatoria", "Cursos": "Cursos", "Información": "Información"}, 
         "English": {"Evento": "Event", "Amazonicas": "Amazonicas", "Programación": "Program", "Organizadores": "Organizers",
                     "Convocatoria": "Call for Papers", "Cursos": "Courses", "Información": "Information"}, 
         "Português": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programação", "Organizadores": "Organizadores",
                       "Convocatoria": "Chamada de artigos", "Cursos": "Coursos", "Información": "Informações"} }

opciones_menu = [
    menus[idioma]["Evento"],
    menus[idioma]["Amazonicas"],
    menus[idioma]["Programación"],
    menus[idioma]["Organizadores"],
    menus[idioma]["Convocatoria"],
    menus[idioma]["Cursos"],
    menus[idioma]["Información"]
]


evento = {
    "Español": {
        "Evento": "AMAZONICAS XI — Congreso Internacional sobre Lenguas Amazónicas",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima",
        "Fechas": "Del 15 al 18 de junio de 2027",
        "Temas": [
            "Fonología: prosodia y entonación",
            "Morfosintaxis: oraciones complejas",
            "Lengua y sociedad: revitalización lingüística en contextos de alta obsolescencia",
            "Sesión general: tema libre"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Lugar",
        "Fechas_label": "Fechas",
        "Correo_label": "Correo",
        "Temas_label": "Temas"
    },

    "English": {
        "Evento": "AMAZONICAS XI — International Conference on Amazonian Languages",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima",
        "Fechas": "June 15–18, 2027",
        "Temas": [
            "Phonology: prosody and intonation",
            "Morphosyntax: complex sentences",
            "Language and Society: language revitalization in high obsolescence contexts",
            "General Session: free topic"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Location",
        "Fechas_label": "Dates",
        "Correo_label": "Email",
        "Temas_label": "Topics"
    },

    "Português": {
        "Evento": "AMAZONICAS XI — Conferência Internacional sobre Línguas Amazónicas",
        "Lugar": "Pontifícia Universidade Católica do Peru, Lima",
        "Fechas": "15 a 18 de junho de 2027",
        "Temas": [
            "Fonologia: prosódia e entoação",
            "Morfossintaxe: cláusulas complexas",
            "Língua e sociedade: revitalização linguística em contextos de elevada obsolescência",
            "Sessão geral: tema livre"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Local",
        "Fechas_label": "Datas",
        "Correo_label": "E-mail",
        "Temas_label": "Temas"
    }
}

opciones = option_menu(
    menu_title=None,
    options=opciones_menu,
    icons=[
        "calendar-event",
        "globe-americas",
        "calendar3",
        "people",
        "megaphone",
        "mortarboard",
        "info-circle"
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if opciones == menus[idioma]["Evento"]: 
    st.markdown( f""" <h2 style=" font-size: 32px; text-align: center; color: #7f3213; "> {evento[idioma]["Evento"]} </h2> """, unsafe_allow_html=True ) 
    st.markdown( f""" <p style="color: #7f3213; font-size: 18px;"> 📍 <strong>{evento[idioma]["Lugar_label"]}:</strong> {evento[idioma]["Lugar"]} </p> <p style="color: #7f3213; font-size: 18px;"> 📅 <strong>{evento[idioma]["Fechas_label"]}:</strong> {evento[idioma]["Fechas"]} </p> <p style="color: #7f3213; font-size: 18px;"> 📧 <strong>{evento[idioma]["Correo_label"]}:</strong> {evento[idioma]["Correo"]} </p> <h3 style="color: #7f3213;"> {evento[idioma]["Temas_label"]} </h3> """, unsafe_allow_html=True ) 
    for tema in evento[idioma]["Temas"]: 
        st.markdown( f""" <p style=" color: #7f3213; font-size: 17px; margin-left: 20px; "> • {tema} </p> """, unsafe_allow_html=True )
        
elif opciones == menus[idioma]["Amazonicas"]: 
  st.header(menus[idioma]["Amazonicas"]) 
  st.write("Información sobre Amazonicas.") 
    
elif opciones == menus[idioma]["Convocatoria"]: 

    st.subheader(subtitulos[idioma]["coordinacion"])
    st.markdown(contenido["coordinacion"])

    st.subheader(subtitulos[idioma]["relativas"])
    st.markdown(contenido["relativas"])

    st.subheader(subtitulos[idioma]["adverbiales"])
    st.markdown(contenido["adverbiales"])

    st.subheader(subtitulos[idioma]["completivas"])
    st.markdown(contenido["completivas"])

    

