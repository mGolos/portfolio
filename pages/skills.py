import tools.utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("Compétences", anchor='skills', divider="orange")
        st.info("En cours d'édition")
        st.markdown(f"""
        """)

    elif sss['language'] == "en":
        st.header("Hard Skills", anchor='skills', divider="orange")
        st.info("Ongoing modifications")
        st.markdown(f"""
        """)
            # - Programming  
            # - :books: Libraries:  
            # ---


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
