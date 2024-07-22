import utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("Compétences", anchor='skills', divider="orange")
        st.markdown(f"""
            (En cours)
        """)

    elif sss['language'] == "en":
        st.header("Hard Skills", anchor='skills', divider="orange")
        st.markdown(f"""
            (In progress)
        """)
            # - Programming  
            # - :books: Libraries:  
            # ---


if __name__ == "__main__":
    utils.always()
    main()
