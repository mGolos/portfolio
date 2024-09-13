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


def download_pdf(url: str, name: str):
    # Checking dates
    if name in sss:
        response = requests.head(url)
        url_date = parsedate(response.headers['Date']).date()
        mem_date = sss[name + '_date']

        # Do not download
        if url_date <= mem_date:
            return sss[name]
    
    # Downloading in memory
    response = requests.get(url)
    pdf_io = BytesIO(response.content)
    
    # Convert to jpg
    pdf = pdfium.PdfDocument(pdf_io)
    page = pdf[0]
    sss[name + '_date'] = parsedate(response.headers['Date']).date()
    sss[name] = image = page.render(scale=4).to_pil()
    return image


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
    '''Once this function is run, it will detect the device's layout (wide or centered)
    and set the 'layout' state accordingly. It also adjusts the width and height
    of the A4 container based on the detected layout.
    '''
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
    index = sss["lg_key"] = languages.index(sss['language'])
    language = st.radio('Language', languages, horizontal=True, label_visibility='hidden', index=index, format_func=countries)
    if sss["language"] != language:
        sss["language"] = language
        st.rerun()


def redirect_button(url: str, icon: str=None, text: str= None, color="transparent"):
    st.markdown(f'''
    <link rel="stylesheet" style="text-decoration: none;" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <a href="{url}" target="_self" style="color: inherit; text-decoration: none;">
        <div style="
                display: flex;
                flex-direction: row;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: start;
                justify-content: flex-start;
                gap: 0.5rem;
                border-radius: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                margin-top: 0.125rem;
                margin-bottom: 0.125rem;
                line-height: 2;
                background-color: {color};
            ">
            <span class="material-symbols-outlined" style="
                    fill: currentcolor;
                    display: inline-flex;
                    -webkit-box-align: center;
                    align-items: center;
                    font-size: 1.25rem;
                    width: 1.25rem;
                    height: 1.25rem;
                    flex-shrink: 0;
                ">
                {icon}
            </span>
            <span style="
                    fcolor: rgb(250, 250, 250);
                    overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                    display: table-cell;
                ">
                {text}
            </span>
        </div>
    </a>
    ''',
    unsafe_allow_html=True)


def pages():
    # https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined&icon.size=24&icon.color=%23e8eaed
    if sss["language"] == 'fr':
        sss['pages'] = {
            "#about": ("A propos", 'person'),
            "#experiences": ("Expériences", 'history'),
            "#education": ("Éducation", 'import_contacts'),
            "#projects": ("Projets", 'content_paste'),
            "#skills": ("Compétences", 'handyman'),
            "#publications": ("Publications", 'history_edu'),
            "#cv": ("Curriculum vitae", 'contact_page'),
            "#recommendations": ("Recommandations", 'mail'),
        }
        
    elif sss["language"] == 'en':
        sss['pages'] = {
            "#about": ("About propos", 'person'),
            "#experiences": ("Experiences", 'history'),
            "#education": ("Education", 'import_contacts'),
            "#projects": ("Projects", 'content_paste'),
            "#skills": ("Skills", 'handyman'),
            "#publications": ("Publications", 'history_edu'),
            "#cv": ("Curriculum vitae", 'contact_page'),
            "#recommendations": ("Recommendations", 'mail'),
        }

    for anchor, (label, icon) in sss['pages'].items():
        redirect_button(anchor, icon=icon, text=label)


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
            [data-testid="stExpanderDetails"] {{
                background: rgb(49 46 33 / 50%);
            }}
            [data-testid="stToolbarActions"] {{
                content-visibility: hidden; 
            }}
            [class="viewerBadge_link__qRIco"] {{
                visibility: hidden; 
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
        """,
        unsafe_allow_html=True,
    )


def once_load_images():
    if 'images' not in sss:
        sss['images'] = {
            name: Image.open(f"images/{name}.jpeg")
            for name in [
                'jl', 'xrator', 'oc', 'lindera', 'ins', 'alpha',
                'rennes', 'amu', 'edu', 'lille', 'iut', 'sup',
            ]
        }


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


def fix_layout():
    if sss['layout'] == 'wide':
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
            div.block-container {
                padding-top: 1.5rem;
                max-width: 55rem;
            }
        </style>
        ''', unsafe_allow_html=True)


def always():
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
    # st.logo(image='images/empty.png', icon_image='images/logoico.png')
    # once_layout_toast()
    once_load_images()
    with st.sidebar:
        sidebar()
    
    fix_layout()
    
    # with open('.streamlit/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
