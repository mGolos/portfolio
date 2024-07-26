import tools.utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("Recommandations", anchor='recommendations', divider="orange")
        tab1, tab2 = st.tabs(["XRator", "INS"])
        
        with tab1:
            utils.iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2179527&authkey=%21ADJYWIi%5FeQVejV4&em=2")
        with tab2:
            utils.iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2178515&authkey=AD4gq0CU3sAJEnk&em=2")

    elif sss['language'] == "en":
        st.header("Recommendations", anchor='recommendations', divider="orange")
        tab1, tab2 = st.tabs(["XRator", "INS"])
        
        with tab1:
            utils.iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2179528&authkey=%21AKf1P7B3SVNyOho&em=2")
        with tab2:
            utils.iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2149593&authkey=AGqw88JCpvqX2_Q&em=2")


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
