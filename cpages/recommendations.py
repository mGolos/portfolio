import streamlit as st
from tools import utils
sss = st.session_state


def main():
    rls = ["LinkedIn", "XRator", "INS"]
    images_names = [f"rl_{rl}_{sss['language']}" for rl in rls]
    
    st.header("Recommandations" if sss["lg_key"] else "Recommendations", anchor='recommendations', divider="orange")
    tabs = st.tabs(rls)
    for tab, image_name in zip(tabs, images_names):
        tab.image(sss['images'][image_name])


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
