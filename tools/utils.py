import os
import base64
import requests
import streamlit as st
import pypdfium2 as pdfium
import streamlit.components.v1 as components
from io import BytesIO
from PIL import Image
from time import sleep
from dateutil.parser import parse as parsedate
from streamlit_js_eval import streamlit_js_eval
sss = st.session_state
sqp = st.query_params


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


@st.cache_resource
# def download_pdf(url: str, name: str):
def download_pdf(lang: str, name: str):
    #TODO Fix the issue created by OneDrive url modification
    # # Checking dates
    # if name in sss:
    #     response = requests.head(url)
    #     url_date = parsedate(response.headers['Date']).date()
    #     mem_date = sss[name + '_date']

    #     # Do not download
    #     if url_date <= mem_date:
    #         return sss[name]
    
    # # Downloading in memory
    # response = requests.get(url)
    # pdf_io = BytesIO(response.content)
    
    # Convert to jpg
    # pdf = pdfium.PdfDocument(pdf_io)
    pdf = pdfium.PdfDocument(f"tools/CV GOLOS {lang}.pdf")
    page = pdf[0]
    # sss[name + '_date'] = parsedate(response.headers['Date']).date()
    sss[name] = image = page.render(scale=4).to_pil()
    return image


def iframe(src:str):
    return components.iframe(src=src, width=sss['a4_width'], height=sss['a4_height'], scrolling=True)

    
def check_layout():
    '''With JS evaluation script, gets the width and height of the device.
    Sleep a little to get the values from JS.
    Then define a layout state depending on which is bigger.
    '''
    width = sss['layout_width'] = streamlit_js_eval(js_expressions='screen.width')
    height = sss['layout_height'] = streamlit_js_eval(js_expressions='screen.height')
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
    '''Once this function is run, it will detect the device's layout (wide or centered)
    and set the 'layout' state accordingly. It also adjusts the width and height
    of the A4 container based on the detected layout.
    '''
    if 'layout_toasted' not in sss:
        st.toast(
            f"{'Narrow' if sss['layout'] == 'wide' else 'Wide'} layout detected. Refresh to reset.", 
            icon = '🛠️')
        sss['layout_toasted'] = True


def countries(s: str):
    match s:
        case 'fr': return ':flag-fr: Français'
        case 'en': return ':flag-gb: English'
    

def language(keyp: str=''):
    languages = ['en', 'fr']
    sqp_lang = sqp.get('language', '')
    sss_lang = sss.get('language', '')
    
    match (sqp_lang in languages, sss_lang in languages):
        case (False, False):
            sqp["language"] = sss["language"] = 'fr'
        case (False, True):
            sqp["language"] = sss["language"]
        case _:
            sss["language"] = sqp["language"]
    
    index = sss["lg_key"] = languages.index(sss['language'])
    # sqp["language"] = language = st.radio(
    #     'Language',
    #     languages, 
    #     key="radio_lang"+keyp, 
    #     horizontal=True, 
    #     label_visibility='hidden', 
    #     index=index, 
    #     format_func=countries,
    # )
    # if sqp["language"] != sss["language"]:
    #     sss["language"] = language
    #     st.rerun()


def menubar():
    # https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined&icon.size=24&icon.color=%23e8eaed
    if sss["language"] == 'fr':
        sss['pages'] = {
            "#about": ("A propos", 'person'),
            "#experiences": ("Expériences", 'history'),
            "#recommendations": ("Recommandations", 'mail'),
            "#education": ("Éducation", 'import_contacts'),
            "#skills": ("Compétences", 'handyman'),
            "#projects": ("Projets", 'content_paste'),
            "#cv": ("CV", 'contact_page'),
            "#publications": ("Publications", 'history_edu'),
            "#contact": ("Contact", 'phone'),
        }
        
    elif sss["language"] == 'en':
        sss['pages'] = {
            "#about": ("About me", 'person'),
            "#experiences": ("Experiences", 'history'),
            "#recommendations": ("Recommendations", 'mail'),
            "#education": ("Education", 'import_contacts'),
            "#skills": ("Skills", 'handyman'),
            "#projects": ("Projects", 'content_paste'),
            "#cv": ("CV", 'contact_page'),
            "#publications": ("Publications", 'history_edu'),
            "#contact": ("Contact", 'phone'),
        }

    menu_html = '<div class="menu-bar"><div class="menu-inner">'
    for anchor, (label, icon) in sss['pages'].items():
        menu_html += (
            f'''<a href="{anchor}" target="_self">
            <span class="material-symbols-outlined">{icon}</span>
            <span>{label}</span>
            </a>'''
        )
    menu_html += '</div></div>'
    st.markdown(menu_html, unsafe_allow_html=True)


def styles():    

    # Inject styles and fonts
    layout = sss.get('layout')
    menu_position = "bottom" if layout == "wide" else "top"
    other_position = "top" if layout == "wide" else "bottom"
    justify_content = "normal" if layout == 'wide' else "center"
    st.markdown(f"""
        <style>
        .menu-bar {{
            position: fixed;
            left: 0;
            width: 100%;
            height: 70px;
            display: flex;
            flex-direction: column;
            justify-content: {justify_content};
            overflow-x: auto;
            padding: 0 0;
            box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
            z-index: 1000;
            {menu_position}: 0;
            border-{other_position}-left-radius: 0.5rem;
            border-{other_position}-right-radius: 0.5rem;
        }}
        .menu-inner {{
            background: linear-gradient(45deg, #001f51, #512400);
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: {justify_content}  ;
            overflow-x: auto;
        }}
        .menu-bar a {{
            color: #ecf0f1;
            text-decoration: none;
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            font-size: 0.75rem;
            min-width: 5rem;
        }}
        .menu-bar .material-symbols-outlined {{
            font-size: 1.5rem;
            margin-bottom: 0.25rem;
        }}

        
        [data-testid="stIFrame"] {{
            border-radius: 0.5rem;
            width: 100%;
            height: calc(min(475px, 48vw));
        }}
        [data-testid="stExpanderDetails"] {{
            background: rgb(49 46 33 / 50%);
        }}
        [data-testid="stHeading"] {{
            # background: linear-gradient(5deg, rgb(237 111 19 / 70%), transparent, transparent)
        }}
        [class="subheader"] {{
            background: linear-gradient(185deg, rgb(237 111 19 / 70%), transparent, transparent)
        }}
        [data-testid="stToolbarActions"] {{
            content-visibility: hidden; 
        }}
        [data-testid="StyledFullScreenButton"] {{
            display: none;
        }}
        [data-testid="baseButton-headerNoPadding"] {{
            color: #ed6f13;
        }}
        [data-testid="stExpanderToggleIcon"] {{
            color: #ed6f13;
        }}
        [class="st-emotion-cache-1wsmgvh eqpbllx1"] {{
            align-items: flex-end; 
        }}
        [class=".stPageLink"]::before {{
            margin-top: -0.5rem;
            margin-bottom: -0.5rem;
        }}
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">""", 
        unsafe_allow_html=True)
    
    
    if layout == 'wide':
        st.write('''
        <style>
            [data-testid="column"] {
                width: calc(16.6666% - 1rem) !important;
                flex: 1 1 calc(16.6666% - 1rem) !important;
                min-width: calc(16.6666% - 1rem) !important;
            }
            .st-emotion-cache-1tpzimh {
                max-width: 20% !important;
            }
            .main{
                position: absolute !important;
            }
        </style>
        ''', unsafe_allow_html=True)
    else:
        st.write('''
        <style>
            [data-testid="column"] {
            }
            .st-emotion-cache-1tpzimh {
                max-width: inherit;
            }
            [data-testid="stMainBlockContainer"] {
                max-width: 55rem;
            }
        </style>
        ''', unsafe_allow_html=True)


@st.cache_resource
def load_image(image_path):
    return Image.open(image_path)


def once_load_images():
    if 'images' not in sss:
        sss['images'] = {
            name.split('.')[0]: load_image(f"images/{name}")
            for name in [
                'refrasense.png', 'jl.jpeg', 'xrator.jpeg', 'oc.jpeg', 'lindera.jpeg', 'ins.jpeg', 'alpha.jpeg',
                'rennes.jpeg', 'amu.jpeg', 'edu.jpeg', 'lille.jpeg', 'iut.jpeg', 'sup.jpeg',
                'p_iut.jpeg', 'p_iut_1.jpeg',
                'p_l3.jpeg', 'p_l3_1.jpeg',
                'p_m1.jpeg', 'p_m1_1.jpeg', 'p_m1_2.jpeg', 'p_m2.jpeg', 'p_m2_1.jpeg',
                'p_m2b.jpeg', 'p_m2b_1.jpeg', 'p_m2b_2.jpeg', 'p_m2b_3.jpeg', 'p_m2b_4.jpeg',
                'p_ocr2.jpeg', 'p_ocr2_1.jpeg',
                'p_ocr3.jpeg', 'p_ocr3_1.jpeg',
                'p_ocr4.jpeg', 'p_ocr4_1.jpeg',
                'p_ocr6.jpeg', 'p_ocr6_1.jpeg', 'p_ocr6_2.jpeg',
                'p_ocr7.jpeg', 'p_ocr7_1.jpeg', 'p_ocr7_2.jpeg', 'p_ocr7_3.jpeg', 'p_ocr7_4.jpeg',
                'p_ocr8.jpeg', 'p_ocr8_1.jpeg',
                'p_mem.jpeg', 'p_motor.jpeg', 'p_motor_1.jpeg', 'p_pal.jpeg',
            ]
        }
        for name in [
                'rl_LinkedIn_en', 'rl_LinkedIn_fr',
                'rl_XRator_en', 'rl_XRator_fr',
                'rl_INS_en', 'rl_INS_fr',
            ]:
            sss['images'][name] = load_image(f"images/{name}.jpg")


@st.cache_resource
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
        sss['bg_x'], sss['bg_y'] = load_image(image_path).size
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
        .stAppHeader {{
            left: 95%;
            background: rgb(0 0 0 / 0%);
            z-index: 9990;
        }}
        .stMain {{
            position: relative;
            z-index: 1;
        }}
        .stMain::before {{
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
            opacity: 0.1;
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
    once_set_layout()
    st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="collapsed",
        page_icon=':scroll:',
        layout=sss['layout'],
        menu_items={
            'About': """
                ## Portfolio of Mathieu Golos
                Mathieu Golos is a Data Scientist with a scientic background in Computational Neurosciences and specialized in Time Series.
            """
        },
    )
    # st.logo(image='images/empty.png', icon_image='images/logoico.png')
    # once_layout_toast()
    once_load_images()
    language()
    styles()
    menubar()
    
    # with open('.streamlit/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
