import utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.markdown(f"""
            # Éducation
            * `[2021]` - **Master Ingénieur Machine Learning**, Centrale Supélec *(Paris)*
            * `[2012]` - **Master Modélisation et Calculs Scientifiques**, Rennes1 *(Rennes)*
            * `[2010]` - **Licence Physique Fondamentale**, Lille1 *(Lille)*
            * `[2008]` - **DUT Mesures Physiques - Génie des matériaux** *(Valenciennes)*
        """)

    elif sss['language'] == "en":
        st.markdown(f"""
            # Education
            * `[2021]` - **Master degree in Machine Learning Engineer**, Centrale Supélec *(Paris)*
            * `[2012]` - **Master degree in Modeling and Scientists Calculus**, Rennes1 *(Rennes)*
            * `[2010]` - **Degree in Fundamental Physics**, Lille1 *(Lille)*
            * `[2008]` - **Technical degree in Physical Measurements - Material Engineering** *(Valenciennes)*
        """)


if __name__ == "__main__":
    utils.always()
    main()
