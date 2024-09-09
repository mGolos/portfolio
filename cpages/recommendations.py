import streamlit as st
from tools import utils
sss = st.session_state


def main():
    lang = sss['language']
    filepath1 = f"data/rl1_{lang}.pdf"
    filepath2 = f"data/rl2_{lang}.pdf"
    down_url = "https://onedrive.live.com/download?{id}&ithint=file%2cpdf"
    
    match lang:
        case "en":
            id1 = "resid=8D406852E7AE31D%2179528&authkey=%21AKf1P7B3SVNyOho"
            id2 = "resid=8D406852E7AE31D%2149593&authkey=AGqw88JCpvqX2_Q"
            st.header("Recommendations", anchor='recommendations', divider="orange")
        case "fr":
            id1 = "resid=8D406852E7AE31D%2179527&authkey=%21ADJYWIi%5FeQVejV4"
            id2 = "resid=8D406852E7AE31D%2178515&authkey=AD4gq0CU3sAJEnk"
            st.header("Recommandations", anchor='recommendations', divider="orange")

    utils.download_pdf(down_url.format(id=id1), filepath1)
    utils.download_pdf(down_url.format(id=id2), filepath2)
    tab1, tab2 = st.tabs(["XRator", "INS"])
    tab1.image(filepath1.replace('.pdf', '.jpg'))
    tab2.image(filepath2.replace('.pdf', '.jpg'))


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
