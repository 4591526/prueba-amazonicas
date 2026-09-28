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

st.markdown(f'<h1 style="font-size: 60px; text-align: center; color: green">Amazonicas</h1>', unsafe_allow_html=True)

idioma = st.selectbox( "Idioma:", ["Español", "English", "Português"] )

menus = { "Español": { "Inicio": "Inicio", "Evento": "Evento", "Amazonicas": "Amazonicas", "Publicaciones": "Publicaciones", "Convocatoria": "Convocatoria" }, 
         "English": { "Inicio": "Home", "Evento": "Event", "Amazonicas": "Amazonicas", "Publicaciones": "Publications", "Convocatoria": "Call for Papers" }, 
         "Português": { "Inicio": "Início", "Evento": "Evento", "Amazonicas": "Amazônicas", "Publicaciones": "Publicações", "Convocatoria": "Chamada" } }


opciones = option_menu( menu_title=None, options=list(menus[idioma].values()), 
                       icons=[ "house", "calendar-event", "globe-americas", "journal-text", "megaphone" ], 
                       menu_icon="cast", default_index=0, orientation="horizontal" )

if opciones == menus[idioma]["Inicio"]: 
  st.header(menus[idioma]["Inicio"]) 
  st.write("Bienvenidos a Amazonicas.") 
elif opciones == menus[idioma]["Evento"]: 
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
