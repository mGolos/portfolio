import streamlit as st
from tools import utils
sss = st.session_state


def main():
    rls = ["XRator", "OC", "INS"]
    filepaths = [f"images/rl{i}_{sss['language'] }.jpg" for i in range(len(rls))][::-1]
    
    st.header("Recommandations" if sss["lg_key"] else "Recommendations", anchor='recommendations', divider="orange")
    tabs = st.tabs(rls)
    for tab, filepath in zip(tabs, filepaths):
        tab.image(filepath)


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
