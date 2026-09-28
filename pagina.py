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
                       "Convocatoria": "Chamada de artigos", "Cursos": "Coursos", "Información": "Informações"} }


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
  st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: green">Amazonicas XI - Call for Papers - Morphosyntax Session: Complex sentences</h2>', unsafe_allow_html=True)
  st.markdown("""
    Complex sentences can be defined differently across linguistic
    frameworks, but they share a common feature: the use of more than
    one verb within a sentence.

    We invite linguists working on Amazonian languages to submit
    abstracts that describe, analyze, or explain **coordination,
    relative clauses, adverbial clauses, or complement clauses** from
    either a synchronic or diachronic perspective.

    **Coordination** involves two independent clauses. In contrast,
    relative, adverbial, and complement clauses are dependent on an
    independent clause.

    In Cristofaro's (2005) typological framework of subordination,
    this dependency must be at least semantic, whereas in formal
    frameworks it is generally understood as syntactic.

    From a typological perspective, it is important to note that not
    all languages make a three-way structural distinction among
    dependent clauses.

    We particularly encourage discussions of the **methodologies used
    to identify, classify, and describe these phenomena**.
    """)

st.subheader("Coordination")

st.markdown("""
    According to Haspelmath (2007), coordinate clauses may contain a
    coordinating element (**syndetic coordination**) or lack one
    (**asyndetic coordination**).

    Syndetic coordination can be classified into eight types depending
    on:

    1. Whether there is one or two elements responsible for the coordination.
    2. The position of these elements with respect to the coordinated clauses.

    From a semantic perspective, coordinating elements may express:

    - conjunction (*and*);
    - disjunction (*or*); or
    - adversative coordination (*but*).
    """)

st.subheader("Relative Clauses")

st.markdown("""
    Relative clauses frequently function as modifiers of noun phrases.
    Structurally, a relative clause contains a **head**, that is, the
    noun phrase modified by the relative clause.

    Two strategies are frequently used to form relative clauses:

    1. The use of a relativizer.
    2. Nominalization.

    Camacho & Gimenez (2017) report that, among 30 Indigenous languages
    analyzed, 18 use nominalization as a relative-clause formation strategy.

    The literature on relative clauses also distinguishes between
    **head-internal** and **head-external** structures.

    Head-external relative clauses may be:

    - **Prenominal** (Relative N), as in Mandarin.
    - **Postnominal** (N Relative), as in English.

    Dryer et al. (2013) analyzed 824 languages and found that 579 have
    postnominal relative clauses, 141 have prenominal relative clauses,
    and 24 have head-internal relative clauses.

    Another typological classification (Payne 1997) considers how the
    noun phrase inside the relative clause, which is coreferential with
    the head, is expressed.

    Two strategies can be distinguished:

    1. **Gap strategy**, in which the noun phrase is not overtly expressed
       inside the relative clause.
    2. **Overt strategy**, in which the noun phrase is phonologically
       expressed inside the relative clause.
    """)

st.subheader("Adverbial Clauses")

st.markdown("""
    Adverbial clauses function as modifiers, or adjuncts, of independent
    clauses. They may express notions such as:

    - time;
    - condition;
    - reason; and
    - purpose or goal.
    """)

st.subheader("Complement Clauses")

st.markdown("""
    Complement clauses function as complements of the verb in the
    independent clause.

    The verbs that select complement clauses may express different
    semantic domains, including:

    - **Modality:** obligation, possibility, capacity.
    - **Phase:** start, stop, continue.
    - **Manipulation:** order, persuade.
    - **Desideratives:** want, desire.
    - **Perception:** hear, see.
    - **Knowledge:** know, perceive.
    - **Propositional attitude:** think, believe.
    - **Enunciation:** say, speak.
    """)


