import streamlit as st
from tools import utils
sss = st.session_state


def main():
    lang = sss['language']
    filepath = f"cv_{lang}.pdf"
    id_en = "resid=08D406852E7AE31D%2193134&authkey=%21AHfSXTlbyrnWlFs"
    id_fr = "resid=08D406852E7AE31D%2193135&authkey=%21AFC4Y6OmO7-GL1g"
    down_url = "https://onedrive.live.com/download?{id}&ithint=file%2cpdf"
    
    st.header("Curriculum vitae", anchor='cv', divider="orange")
    match lang:
        case "en":
            id_ = id_en
            st.markdown(
                "Download in pdf the "
                f"[english version]({down_url.format(id=id_en)}) | "
                f"[french version]({down_url.format(id=id_fr)})"
            )
        case "fr": 
            id_ = id_fr
            st.markdown(
                "Télécharger en pdf la version "
                f"[française]({down_url.format(id=id_fr)}) | "
                f"[anglaise]({down_url.format(id=id_en)})"
            )
    
    image = utils.download_pdf(down_url.format(id=id_), filepath)
    st.image(image)


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
