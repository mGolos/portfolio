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
        st.header("Comment me contacter ?", anchor='contact', divider="orange")
        st.markdown("""
            La meilleur façon de me joindre est par email.
        """)
    elif sss["language"] == "en":
        st.header("How to reach me?", anchor='contact', divider="orange")
        st.markdown("""
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
            icon = '🛠️')
        sss['layout_toasted'] = True


def sidebar():        
    add_logo_N_styles()
    language()
    st.header("Mathieu Golos", divider="orange")
    pages()
    st.subheader("", divider="orange")
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
    if 'profile_img' not in sss:
        sss['profile_img'] = base64.b64encode(open('images/profile.png', "rb").read()).decode()
    
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarUserContent"] {{
                background-image: url(data:image/png;base64,{sss['profile_img']});
                background-repeat: no-repeat;
                padding-top: 80px;
                background-size: 150px;
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
                'rennes', 'amu', 'lille', 'iut', 'sup',
            ]
        }


def once_meta():
    if 'meta' not in sss:
        from pathlib import Path
        import re
        
        index = Path(st.__file__).parent / "static" / "index.html"
        html = index.read_text()
        
        title = '<title>Mathieu Golos - portoflio</title>'
        meta = (
            '<meta name="title" content="Mathieu Golos - portoflio">'
            '<meta name="description" content="Mathieu Golos is a Data Scientist with a scientic background in Computational Neurosciences and specialized in Time Series.">'
        )
        
        balise = '<meta charset="UTF-8"/>'
        html = re.sub(r'(?s)<title>.*?</title>', title, html)
        html = html.replace(balise, balise+meta)
        index.write_text(html)
        sss['meta'] = True


def get_base64_image(image_path):
    with open(image_path, 'rb') as img_file:
        img_bytes = img_file.read()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_base64


def background():
    ''' Calling it at the end otherwise it creates a visual element that put everything down.
    (scroll bar event missing)
    '''
    if 'bg_64' not in sss:
        image_path = 'images/bg.jpeg'
        sss['bg_x'], sss['bg_y'] = Image.open(image_path).size
        sss['bg_64'] = get_base64_image(image_path)
        sss['bg_ext'] = image_path.rsplit('.', 1)[1]
    
    style_code = (f"""
        <style>
        :root {{
            --parallax-bg-position: center 0px;
            --parallax-bg-height: {sss['bg_x']}px;
            --parallax-bg-width: {sss['bg_y']}px;
        }}
        .stApp {{
            background: transparent !important;
        }}
        .main {{
            position: relative;
            z-index: 1;
        }}
        .main::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url(data:image/{sss['bg_ext']};base64,{sss['bg_64']});
            background-repeat: no-repeat;
            background-position: var(--parallax-bg-position, 0px 0px);
            background-size: var(--parallax-bg-width) var(--parallax-bg-height);
            opacity: 0.13;
            z-index: -1;
            transition: background-position 1s ease-out;
            animation: breath 4s ease-in-out alternate infinite;
        }}
        @keyframes breath {{
            from {{
                transform: scale(1);
            }}
            to {{
                transform: scale(1.1);
            }}
        }}
        </style>
    """)
    js_code = f"""
    <script>
        const mainElement = parent.document.querySelector('.main');
        const blockElement = parent.document.querySelector('.block-container');
        const bgImageHeight = {sss['bg_x']};
        const reduce = 4
        
        function updateScale() {{
            mainElement.style.setProperty('--parallax-bg-position', `center 0px`);
            var offsetHeight = mainElement.offsetHeight;
            var blockHeight = blockElement.scrollHeight;
            var screenHeight = screen.height;
            var bgScale = bgImageHeight / screenHeight / reduce;
            mainElement.style.setProperty('--parallax-bg-height', `${{{sss['bg_x']} * bgScale}}px`);
            mainElement.style.setProperty('--parallax-bg-width', `${{{sss['bg_y']} * bgScale}}px`);
            return bgScale
        }};
        const bgScale = updateScale();
        
        function updateParallax() {{
            var scroll = mainElement.scrollTop;
            var mainHeight = mainElement.offsetHeight;
            var blockHeight = blockElement.scrollHeight;
            
            var scrollMax = blockHeight - mainHeight;
            var positionMax = bgImageHeight * bgScale - mainHeight;
            var ratio = positionMax / scrollMax;
            
            if (ratio < 0) {{
                var position = scroll * ratio;
            }}
            if (ratio >= 0) {{
                var position = - scroll * ratio;
            }}
            mainElement.style.setProperty('--parallax-bg-position', `center ${{position}}px`);
        }};
        
        parent.window.addEventListener('wheel', updateParallax);
        parent.window.addEventListener('scroll', updateParallax);
        parent.window.addEventListener('touchmove', updateParallax);
    </script>
    """ 
    st.components.v1.html(js_code, height=0)
    st.markdown(style_code, unsafe_allow_html=True)


def always():
    once_meta()
    once_set_layout()
    state = st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="auto",
        page_icon=':scroll:',
        layout=sss['layout'],
        menu_items={
            'About': """
                ## Portfolio of Mathieu Golos
                Mathieu Golos is a Data Scientist with a scientic background in Computational Neurosciences and specialized in Time Series.
            """
        },
    )
    once_layout_toast()
    once_load_images()
    with st.sidebar:
        sidebar()
    
    # with open('.streamlit/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
