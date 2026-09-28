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

st.markdown(f'<h1 style="font-size: 60px; text-align: center; color: green">Amazonicas XI</h1>', unsafe_allow_html=True)

idioma = st.selectbox( "Idioma:", ["Español", "English", "Português"] )

menus = { "Español": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programación", "Organizadores": "Organizadores", 
                      "Convocatoria": "Convocatoria", "Cursos": "Cursos", "Información": "Información"}, 
         "English": {"Evento": "Event", "Amazonicas": "Amazonicas", "Programación": "Program", "Organizadores": "Organizers",
                     "Convocatoria": "Call for Papers", "Cursos": "Courses", "Información": "Information"}, 
         "Português": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programação", "Organizadores": "Organizadores",
                       "Convocatoria": "Chamada para trabalhos", "Cursos": "Coursos", "Información": "Informações"} }


opciones = option_menu(
    menu_title=None,
    options=[
        "Evento",
        "Amazonicas",
        "Programación",
        "Organizadores",
        "Convocatoria",
        "Cursos",
        "Información"
    ],
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
  st.header(menus[idioma]["Evento"]) 
  st.write("Información sobre el evento.") 
elif opciones == menus[idioma]["Amazonicas"]: 
  st.header(menus[idioma]["Amazonicas"]) 
  st.write("Información sobre Amazonicas.") 
elif opciones == menus[idioma]["Publicaciones"]: 
  st.header(menus[idioma]["Publicaciones"]) 
  st.write("Publicaciones y recursos.") 
elif opciones == menus[idioma]["Convocatoria"]: 
  st.header(menus[idioma]["Convocatoria"]) 
  st.write("Información sobre la convocatoria.")
