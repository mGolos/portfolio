import utils
import streamlit as st
sss = st.session_state


def main():
    xrator = "[XRator](https://www.x-rator.com/)"
    lindera = "[Lindera](https://www.lindera.de/)"
    jl = "[Jagger&Lewis](https://www.jagger-lewis.com/)"

    if sss['language'] == "fr":
        st.markdown(f"""
            # Expériences
            * `[2023] (1 an)` - **Scientifique de la donnée**, {jl} *(France)*
            * `[2023] (2 mois)` - **Scientifique de la donnée Clinique**, {lindera} *(Italie/Allemagne)*
            * `[2022] (9 mois)` - **Scientifique de la donnée**, {xrator} *(France/Vietnam)*
            * `[2021] (8 mois)` - **Stage Ingénieur Machine Learning**, OpenClassrooms *(Lille)*
            * `[2019 - 2020] (7 mois)` - **Ingénieur DevOps**, Alpha Conseils *(St-Germain-en-Laye)*
            * `[2013 - 2017] (4 ans)` - **Doctorant en Neurosciences Computationnelles**, INS/INSERM 1106 *(Marseille)*
            * `[2013] (9 mois)` - **Assistant Ingénieur**, INS, INSERM 1106 *(Marseille)*
        """)

    elif sss['language'] == "en":
        st.markdown(f"""
            # Experiences
            * `[2023] (1 year)` - **Data Scientist**, {jl} *(France)*
            * `[2023] (2 months)` - **Data Scientist Clinical**, {lindera} *(Italy/Germany)*
            * `[2022] (9 months)` - **Data Scientist**, {xrator} *(France/Vietnam)*
            * `[2021] (8 months)` - **Machine Learning Engineer (Internship)**, OpenClassrooms *(Lille)*
            * `[2019 - 2020] (7 months)` - **DevOps Engineer**, Alpha Conseils *(St-Germain-en-Laye)*
            * `[2013 - 2017] (4 years)` - **PhD Candidate in Computational Neurosciences**, INS/INSERM 1106 *(Marseille)*
            * `[2013] (9 months)` - **Assistant Engineer**, INS, INSERM 1106 *(Marseille)*
        """)


if __name__ == "__main__":
    utils.always()
    main()
