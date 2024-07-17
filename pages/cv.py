import os
import utils
import base64
import requests
import streamlit as st
from datetime import datetime
from dateutil.parser import parse as parsedate
sss = st.session_state


def download(url: str, filename: str):
    # Checking dates
    if os.path.exists(filename):
        r = requests.head(url)
        url_date = parsedate(r.headers['Date']).date()
        file_date = datetime.fromtimestamp(os.path.getmtime(filename)).date()

        # Do not download
        if url_date <= file_date:
            return None
    
    # Downloading
    response = requests.get(url)
    with open(filename, 'wb') as output:
        output.write(response.content)


def display(url: str):
    st.markdown(f"""<iframe
        src="{url}"
        width="100%"
        height="1020px"
    ></iframe>""", unsafe_allow_html=True)


def main():
    lang = sss['language']
    filename = f"data/cv_{lang}.pdf"
    id_en = "resid=8D406852E7AE31D%2186868&authkey=!AEfRPV4nuAuTXyc"
    id_fr = "resid=8D406852E7AE31D%2186859&authkey=!AFtjbavPucqp6mk"
    visu_url = "https://onedrive.live.com/embed?cid=08D406852E7AE31D&{id}&em=2"
    down_url = "https://onedrive.live.com/download?{id}&ithint=file%2cpdf"
    
    st.markdown("# Curriculum vitae")
    match lang:
        case "en":
            id_ = id_en
            st.markdown(
                "Download the "
                f"[english version]({down_url.format(id=id_en)}) | "
                f"[french version]({down_url.format(id=id_fr)})"
            )
        case "fr": 
            id_ = id_fr
            st.markdown(
                "Télécharger la version "
                f"[française]({down_url.format(id=id_fr)}) | "
                f"[anglaise]({down_url.format(id=id_en)})"
            )
    
    # display(visu_url.format(id=id_))
    
    # File
    download(down_url.format(id=id_), filename)
    with open(filename, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1200" type="application/pdf"></iframe>'
        # # # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1020" type="application/pdf"></iframe>'
        # st.markdown(pdf_display, unsafe_allow_html=True)
        
    from streamlit_js_eval import streamlit_js_eval
    width = str(streamlit_js_eval(js_expressions="window.innerWidth") - 10)
    height = "100px"
    
    st.markdown(f"""## Any image\n <iframe
        src="images/logo.png"
        width="{width}" height="{height}"
    ></iframe>""", unsafe_allow_html=True)
    st.markdown(f"""## Loaded embed\n <embed
        src="data:application/pdf;base64,{base64_pdf}"
        width="{width}" height="{height}"
        class="pdfobject"
        type="application/pdf"
    ></embed>""", unsafe_allow_html=True)
    st.markdown(f"""## Filename embed\n <embed
        src="data/cv_{lang}.pdf"
        width="{width}" height="{height}"
        class="pdfobject"
        type="application/pdf"
    ></embed>""", unsafe_allow_html=True)
    
    st.markdown(f"""## Filename iframe\n <iframe
        src="data/cv_{lang}.pdf"
        width="{width}" height="{height}"
        type="application/pdf"
    ></iframe>""", unsafe_allow_html=True)
    st.markdown(f"""## Loaded iframe\n <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="{width}" height="{height}"
        type="application/pdf"
    ></iframe>""", unsafe_allow_html=True)
    st.markdown(f"""## Online iframe\n <iframe
        src="{visu_url.format(id=id_)}"
        width="{width}" height="{height}"
        type="application/pdf"
    ></iframe>""", unsafe_allow_html=True)


if __name__ == "__main__":
    utils.always()
    main()
