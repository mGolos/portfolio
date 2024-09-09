import streamlit as st
from tools import utils
sss = st.session_state


def main():
    lang = sss['language']
    filepath1 = f"images/rl1_{lang}.jpg"
    filepath2 = f"images/rl2_{lang}.jpg"
    
    st.header("Recommandations" if sss["lg_key"] else "Recommendations", anchor='recommendations', divider="orange")
    tab1, tab2 = st.tabs(["XRator", "INS"])
    tab1.image(filepath1)
    tab2.image(filepath2)


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
