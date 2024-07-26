import streamlit as st
from tools import utils
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
            
            # * Technologies :
            # Machine Learning, Deep learning, NLP,Backend Developer
            # * Languages :
            # Python, C, C++, Java, SQL, Bash Script
            # * Frameworks :
            # TensorFlow, Scikit, NLTK, SpaCy, Keras, Flask, Sreamlit, Java Swing, Springboot
            # * Soft Skills :
            # Leadership, Creativity, Writing, Public Speaking, Time Management, Problem Solving, Communications


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
