import base64
import streamlit as st
import streamlit.components.v1 as components
from time import sleep
from streamlit_js_eval import streamlit_js_eval
sss = st.session_state


contact = """
    :globe_with_meridians: [LinkedIn](https://www.linkedin.com/in/mathieu-golos-25055b77/)  
    :email: [mathieu.golos@gmail.com](mail:mathieu.golos@gmail.com)  
    :telephone_receiver: [+33611478901](tel:+33611478901)  
    :earth_africa: [Lille (FRANCE)](https://goo.gl/maps/eXC8BJh9qGXWBgZDA)  
"""


def footer():
    if sss["language"] == "fr":
        st.markdown("""
            # Comment me contacter ?
            La meilleur façon de me joindre est par email.
        """)
    elif sss["language"] == "en":
        st.markdown("""
            # How to reach me?
            The best way to contact me is by email.
        """)
    st.write(contact)


def iframe(src:str):
    return components.iframe(src=src, width=None, height=1020, scrolling=True)

    
def check_layout():
    '''With JS evaluation script, gets the width and height of the device.
    Sleep a little to get the values from JS.
    Then define a layout state depending on which is bigger.
    '''
    width = streamlit_js_eval(js_expressions='screen.width')
    height = streamlit_js_eval(js_expressions='screen.height')
    sleep(1)
        
    if width is not None and height is not None:
        sss['layout'] = "wide" if width < height else "centered"


def once_set_layout():
    '''Search for the device layout and rerun once set.
    '''
    if 'layout' not in sss:
        with st.spinner('Checking your device layout...'):
            check_layout()
            st.rerun()


def once_layout_toast():
    if 'layout_toasted' not in sss:
        st.toast(f"{'Narrow' if sss['layout'] == 'wide' else 'Wide'} layout detected.")
        sss['layout_toasted'] = True


# @st.experimental_fragment
def sidebar():
    if 'nrun' not in sss:
        sss['nrun'] = 1
    else:
        sss['nrun'] += 1
        
    language()

    add_logo_N_styles()
    st.logo('images/empty.png', icon_image='images/logo.png')

    for filename, (label, icon) in sss['pages'].items():
        st.page_link(filename, label=label, icon=icon)
        
    # st.page_link("https://www.linkedin.com/in/mathieu-golos-25055b77", label="LinkedIn", icon='🌍')
    # st.write('---')   
    st.markdown(contact)
    
    print(sss['nrun'])


def countries(s: str):
    match s:
        case 'fr': return ':flag-fr: Français'
        case 'en': return ':flag-gb: English'
    

# @st.experimental_fragment
def language():
    languages = ['en', 'fr']
    index = languages.index(sss['language']) if "language" in sss else 0
    st.info(sss["language"]) if "language" in sss else st.info('no language')
    
    # st.sidebar.radio('Language', languages, horizontal=True, label_visibility='hidden', key='language', format_func=countries)
    sss["language"] = st.radio('Language', languages, horizontal=True, label_visibility='hidden', index=index, format_func=countries)
    st.info(sss["language"])
    # st.rerun()
    
    if sss["language"] == 'fr':
        sss["pages"] = {
            "app.py": ("Tout", '🧻'),
            "pages/about.py": ("A propos", '❔'),
            "pages/journey.py": ("Parcours", '🏃'),
            "pages/projects.py": ("Projets", '🔧'),
            "pages/timeline.py": ("Chronologie", '🎞️'),
            "pages/publications.py": ("Publications", '📜'),
            "pages/cv.py": ("Curriculum vitae", '📄'),
            "pages/recommendations.py": ("Recommandations", '💌'),
        }
        
    elif sss["language"] == 'en':
        sss["pages"] = {
            "app.py": ("All", '🧻'),
            "pages/about.py": ("About", '❔'),
            "pages/journey.py": ("Journey", '🏃'),
            "pages/projects.py": ("Projects", '🔧'),
            "pages/timeline.py": ("Timeline", '🎞️'),
            "pages/publications.py": ("Publications", '📜'),
            "pages/cv.py": ("Curriculum vitae", '📄'),
            "pages/recommendations.py": ("Recommendations", '💌'),
        }


def add_logo_N_styles():
    image_str = base64.b64encode(open('images/logo.png', "rb").read()).decode()
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarUserContent"] {{
                background-image: url(data:image/png;base64,{image_str});
                background-repeat: no-repeat;
                padding-top: 100px;
                background-size: 240px;
                background-position: 20px 0px;
            }}
            [data-testid="stSidebarUserContent"]::before {{
                content: "";
                margin-left: 20px;
                font-size: 10px;
            }}
            [data-testid="stSidebarHeader"] {{
                padding: 0rem 0rem 0rem;
                # padding: 0.5rem 0.5rem 0.5rem;
            }}
            [data-testid="stHeader"] {{
                height: 0;
            }}
            [class=".stPageLink"]::before {{
                margin-top: -0.5rem;
                margin-bottom: -0.5rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def always():
    once_set_layout()
    state = st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="collapsed" if sss['layout'] == 'wide' else "expanded",
        page_icon=':scroll:',
        layout=sss['layout'],
    )
    once_layout_toast()
    with st.sidebar:
        sidebar()
    
    # with open('.streamlit/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
