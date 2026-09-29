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
    st.image("banner_amazonicas.png", width=1500)
        
#st.markdown(f'<h1 style="font-size: 60px; text-align: center; color: green">Amazonicas XI</h1>', unsafe_allow_html=True)

idioma = st.selectbox( "Idioma:", ["Español", "English", "Português"] )

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

titulo_convocatoria = {
    "Español": "Amazonicas XI - Convocatoria - Sesión de Morfosintaxis: Oraciones complejas",
    "English": "Amazonicas XI - Call for Papers - Morphosyntax Session: Complex Sentences",
    "Português": "Amazonicas XI - Chamada para trabalhos - Sessão de Morfossintaxe: Orações complexas"
}

contenido_convocatoria = {
    "Español": {
    
            "introduccion": """
    Las oraciones complejas pueden definirse de diferentes maneras
    según el marco lingüístico, pero comparten una característica:
    el uso de más de un verbo dentro de una oración.
    
    Invitamos a lingüistas que trabajan con lenguas amazónicas a
    presentar resúmenes que describan, analicen o expliquen la
    **coordinación, las cláusulas relativas, las cláusulas adverbiales
    o las cláusulas completivas**, desde una perspectiva sincrónica
    o diacrónica.
    
    La **coordinación** involucra dos cláusulas independientes. En
    cambio, las cláusulas relativas, adverbiales y completivas dependen
    de una cláusula independiente.
    
    En el marco tipológico de la subordinación de Cristofaro (2005),
    esta dependencia debe ser, al menos, semántica, mientras que en
    los marcos formales generalmente se entiende como sintáctica.
    
    Desde una perspectiva tipológica, es importante señalar que no
    todas las lenguas establecen una distinción estructural tripartita
    entre sus cláusulas dependientes.
    
    También se alienta especialmente la presentación de trabajos sobre
    las **metodologías utilizadas para identificar, clasificar y
    describir estos fenómenos**.
    """,
    
            "coordinacion": """
    Según Haspelmath (2007), las cláusulas coordinadas pueden presentar
    un elemento coordinante (**coordinación sindética**) o no presentar
    ninguno (**coordinación asindética**).
    
    La coordinación sindética puede clasificarse en ocho tipos según:
    
    1. Si existe uno o dos elementos responsables de la coordinación.
    2. La posición de estos elementos con respecto a las cláusulas coordinadas.
    
    Desde una perspectiva semántica, los elementos coordinantes pueden
    expresar:
    
    - conjunción (*y*);
    - disyunción (*o*); o
    - coordinación adversativa (*pero*).
    """,
    
            "relativas": """
    Las cláusulas relativas suelen funcionar como modificadores de
    sintagmas nominales. Estructuralmente, una cláusula relativa
    contiene un **núcleo**, es decir, el sintagma nominal modificado
    por la cláusula relativa.
    
    Dos estrategias se utilizan frecuentemente para formar cláusulas
    relativas:
    
    1. El uso de un relativizador.
    2. La nominalización.
    
    Camacho & Gimenez (2017) señalan que, entre 30 lenguas indígenas
    analizadas, 18 utilizan la nominalización como estrategia para
    formar cláusulas relativas.
    
    La literatura sobre cláusulas relativas también distingue entre
    estructuras de **núcleo interno** y **núcleo externo**.
    
    Las cláusulas relativas de núcleo externo pueden ser:
    
    - **Prenominales** (Relativa N), como en mandarín.
    - **Posnominales** (N Relativa), como en inglés.
    
    Dryer et al. (2013) analizaron 824 lenguas y encontraron que 579
    presentan relativas posnominales, 141 relativas prenominales y
    24 relativas de núcleo interno.
    
    Otra clasificación tipológica (Payne 1997) considera cómo se
    expresa el sintagma nominal dentro de la cláusula relativa que
    es correferencial con el núcleo.
    
    Se pueden distinguir dos estrategias:
    
    1. **Estrategia de posición vacía (gap)**, en la que el sintagma
       nominal no se expresa dentro de la cláusula relativa.
    2. **Estrategia manifiesta (overt)**, en la que el sintagma nominal
       se expresa fonológicamente dentro de la cláusula relativa.
    """,
    
            "adverbiales": """
    Las cláusulas adverbiales funcionan como modificadores o adjuntos
    de cláusulas independientes. Pueden expresar nociones como:
    
    - tiempo;
    - condición;
    - razón; y
    - propósito o finalidad.
    """,
    
            "completivas": """
    Las cláusulas completivas funcionan como complementos del verbo
    de la cláusula independiente.
    
    Los verbos que seleccionan cláusulas completivas pueden expresar
    diferentes dominios semánticos:
    
    - **Modalidad:** obligación, posibilidad, capacidad.
    - **Fase:** comenzar, detenerse, continuar.
    - **Manipulación:** ordenar, persuadir.
    - **Desiderativos:** querer, desear.
    - **Percepción:** oír, ver.
    - **Conocimiento:** saber, percibir.
    - **Actitud proposicional:** pensar, creer.
    - **Enunciación:** decir, hablar.
    """
        },
        
    "English": {

            "introduccion": """
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
    """,
    
            "coordinacion": """
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
    """,
    
            "relativas": """
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
    """,
    
            "adverbiales": """
    Adverbial clauses function as modifiers, or adjuncts, of independent
    clauses. They may express notions such as:
    
    - time;
    - condition;
    - reason; and
    - purpose or goal.
    """,
    
            "completivas": """
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
    """
        }, 
   
    "Português": {
    
            "introduccion": """
    As orações complexas podem ser definidas de diferentes maneiras
    de acordo com o referencial linguístico adotado, mas compartilham
    uma característica: o uso de mais de um verbo em uma oração.
    
    Convidamos linguistas que trabalham com línguas amazônicas a
    enviar resumos que descrevam, analisem ou expliquem a
    **coordenação, as orações relativas, as orações adverbiais ou as
    orações completivas**, a partir de uma perspectiva sincrônica
    ou diacrônica.
    
    A **coordenação** envolve duas orações independentes. Por outro
    lado, as orações relativas, adverbiais e completivas são
    dependentes de uma oração independente.
    
    No quadro tipológico de subordinação de Cristofaro (2005), essa
    dependência deve ser, pelo menos, semântica, enquanto nos
    referenciais formais ela é geralmente entendida como sintática.
    
    Do ponto de vista tipológico, é importante observar que nem todas
    as línguas estabelecem uma distinção estrutural tripla entre suas
    orações dependentes.
    
    Também são especialmente bem-vindos trabalhos que discutam as
    **metodologias utilizadas para identificar, classificar e descrever
    esses fenômenos**.
    """,
    
            "coordinacion": """
    De acordo com Haspelmath (2007), as orações coordenadas podem
    apresentar um elemento coordenador (**coordenação sindética**) ou
    não apresentar um elemento coordenador (**coordenação assindética**).
    
    A coordenação sindética pode ser classificada em oito tipos de acordo com:
    
    1. A existência de um ou dois elementos responsáveis pela coordenação.
    2. A posição desses elementos em relação às orações coordenadas.
    
    Do ponto de vista semântico, os elementos coordenadores podem expressar:
    
    - conjunção (*e*);
    - disjunção (*ou*); ou
    - coordenação adversativa (*mas*).
    """,
    
            "relativas": """
    As orações relativas frequentemente funcionam como modificadores
    de sintagmas nominais. Estruturalmente, uma oração relativa contém
    um **núcleo**, isto é, o sintagma nominal modificado pela oração relativa.
    
    Duas estratégias são frequentemente utilizadas para formar orações relativas:
    
    1. O uso de um relativizador.
    2. A nominalização.
    
    Camacho & Gimenez (2017) relatam que, entre 30 línguas indígenas
    analisadas, 18 utilizam a nominalização como estratégia de formação
    de orações relativas.
    
    A literatura sobre orações relativas também distingue estruturas
    de **núcleo interno** e **núcleo externo**.
    
    As orações relativas de núcleo externo podem ser:
    
    - **Prenominais** (Relativa N), como no mandarim.
    - **Pós-nominais** (N Relativa), como no inglês.
    
    Dryer et al. (2013) analisaram 824 línguas e encontraram 579 com
    relativas pós-nominais, 141 com relativas prenominais e 24 com
    relativas de núcleo interno.
    
    Outra classificação tipológica (Payne 1997) considera a maneira
    como o sintagma nominal dentro da oração relativa, correferente
    ao núcleo, é expresso.
    
    Duas estratégias podem ser distinguidas:
    
    1. **Estratégia de lacuna (gap)**, em que o sintagma nominal não é
       expresso dentro da oração relativa.
    2. **Estratégia explícita (overt)**, em que o sintagma nominal é
       expresso fonologicamente dentro da oração relativa.
    """,
    
            "adverbiales": """
    As orações adverbiais funcionam como modificadores ou adjuntos
    de orações independentes. Elas podem expressar noções como:
    
    - tempo;
    - condição;
    - razão; e
    - propósito ou finalidade.
    """,
    
            "completivas": """
    As orações completivas funcionam como complementos do verbo da
    oração independente.
    
    Os verbos que selecionam orações completivas podem expressar
    diferentes domínios semânticos:
    
    - **Modalidade:** obrigação, possibilidade, capacidade.
    - **Fase:** começar, parar, continuar.
    - **Manipulação:** ordenar, persuadir.
    - **Desiderativos:** querer, desejar.
    - **Percepção:** ouvir, ver.
    - **Conhecimento:** saber, perceber.
    - **Atitude proposicional:** pensar, acreditar.
    - **Enunciação:** dizer, falar.
    """
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
  st.header(menus[idioma]["Evento"]) 
  st.write("Información sobre el evento.") 
elif opciones == menus[idioma]["Amazonicas"]: 
  st.header(menus[idioma]["Amazonicas"]) 
  st.write("Información sobre Amazonicas.") 
    
elif opciones == menus[idioma]["Convocatoria"]: 
    st.markdown(
        f"""
        <h2 style="
            font-size: 32px;
            text-align: center;
            color: #2E7D32;
        ">
        {titulo_convocatoria[idioma]}
        </h2>
        """,
        unsafe_allow_html=True
        )
    
    contenido = contenido_convocatoria[idioma]

    st.markdown(contenido["introduccion"])

    subtitulos = {
        "Español": {
            "coordinacion": "Coordinación",
            "relativas": "Cláusulas relativas",
            "adverbiales": "Cláusulas adverbiales",
            "completivas": "Cláusulas completivas"
        },

        "English": {
            "coordinacion": "Coordination",
            "relativas": "Relative Clauses",
            "adverbiales": "Adverbial Clauses",
            "completivas": "Complement Clauses"
        },

        "Português": {
            "coordinacion": "Coordenação",
            "relativas": "Orações relativas",
            "adverbiales": "Orações adverbiais",
            "completivas": "Orações completivas"
        }
    }

    st.subheader(subtitulos[idioma]["coordinacion"])
    st.markdown(contenido["coordinacion"])

    st.subheader(subtitulos[idioma]["relativas"])
    st.markdown(contenido["relativas"])

    st.subheader(subtitulos[idioma]["adverbiales"])
    st.markdown(contenido["adverbiales"])

    st.subheader(subtitulos[idioma]["completivas"])
    st.markdown(contenido["completivas"])

    

