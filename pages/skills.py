import utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.markdown(f"""
            # Compétences
            (En cours)
        """)

    elif sss['language'] == "en":
        st.markdown(f"""
            # Hard Skills
            (In progress)
        """)
            # - Programming  
            # - :books: Libraries:  
            # ---


if __name__ == "__main__":
    utils.always()
    main()
