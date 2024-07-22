import base64
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
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
    return components.iframe(src=src, width=sss['a4_width'], height=sss['a4_height'], scrolling=True)

    
def check_layout():
    '''With JS evaluation script, gets the width and height of the device.
    Sleep a little to get the values from JS.
    Then define a layout state depending on which is bigger.
    '''
    width = streamlit_js_eval(js_expressions='screen.width')
    height = streamlit_js_eval(js_expressions='screen.height')
    inner_width = streamlit_js_eval(js_expressions="window.innerWidth")
    sleep(1)
        
    if width is not None and height is not None:
        if width < height:
            # portrait
            sss['layout'] = "wide"
            sss['a4_width'] = int(width * 0.92)
            sss['a4_height'] = 700
        else:
            # landscape
            sss['layout'] = "centered"
            sss['a4_width'] = inner_width
            sss['a4_height'] = 1020


def once_set_layout():
    '''Search for the device layout and rerun once set.
    '''
    if 'layout' not in sss:
        with st.spinner('Checking your device layout...'):
            check_layout()
            st.rerun()


def once_layout_toast():
    if 'layout_toasted' not in sss:
        st.toast(
            f"{'Narrow' if sss['layout'] == 'wide' else 'Wide'} layout detected. Refresh to reset.", 
            icon = '🪟')
        sss['layout_toasted'] = True


def sidebar():        
    add_logo_N_styles()
    language()
    st.write('# Mathieu Golos')
    pages()
    st.write('---')
    st.markdown(contact)


def countries(s: str):
    match s:
        case 'fr': return ':flag-fr: Français'
        case 'en': return ':flag-gb: English'
    

def language():
    if 'language' not in sss:
        sss["language"] = 'fr'
    
    languages = ['en', 'fr']
    index = languages.index(sss['language'])
    language = st.radio('Language', languages, horizontal=True, label_visibility='hidden', index=index, format_func=countries)
    if sss["language"] != language:
        sss["language"] = language
        st.rerun()


def pages():
    # https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined&icon.size=24&icon.color=%23e8eaed
    if sss["language"] == 'fr':
        sss['pages'] = {
            "app.py": ("Tout", ':material/scrollable_header:'),
            "pages/about.py": ("A propos", ':material/person:'),
            "pages/experiences.py": ("Expériences", ':material/history:'),
            "pages/education.py": ("Éducation", ':material/import_contacts:'),
            "pages/projects.py": ("Projets", ':material/content_paste:'),
            "pages/skills.py": ("Compétences", ':material/handyman:'),
            "pages/publications.py": ("Publications", ':material/history_edu:'),
            "pages/recommendations.py": ("Recommandations", ':material/mail:'),
            "pages/cv.py": ("Curriculum vitae", ':material/contact_page:'),
        }
        
    elif sss["language"] == 'en':
        sss['pages'] = {
            "app.py": ("All", ':material/scrollable_header:'),
            "pages/about.py": ("About", ':material/person:'),
            "pages/experiences.py": ("Experiences", ':material/history:'),
            "pages/education.py": ("Education", ':material/import_contacts:'),
            "pages/projects.py": ("Projects", ':material/content_paste:'),
            "pages/skills.py": ("Skills", ':material/handyman:'),
            "pages/publications.py": ("Publications", ':material/history_edu:'),
            "pages/recommendations.py": ("Recommendations", ':material/mail:'),
            "pages/cv.py": ("Curriculum vitae", ':material/contact_page:'),
        }

    for filename, (label, icon) in sss['pages'].items():
        st.page_link(filename, label=label, icon=icon)


def add_logo_N_styles():
    st.logo('images/empty.png', icon_image='images/logo.png')
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


def once_load_images():
    if 'images' not in sss:
        sss['images'] = {
            name: Image.open(f"images/{name}.jpeg")
            for name in [
                'jl', 'xrator', 'oc', 'lindera', 'ins', 'alpha',
                'rennes', 'lille', 'iut', 'sup',
            ]
        }


def always():
    once_set_layout()
    state = st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="collapsed" if sss['layout'] == 'wide' else "expanded",
        page_icon=':scroll:',
        layout=sss['layout'],
    )
    once_layout_toast()
    once_load_images()
    with st.sidebar:
        sidebar()
    
    # with open('.streamlit/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
