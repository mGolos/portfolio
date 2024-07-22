import utils
import streamlit as st
sss = st.session_state


def main():        
    link1 = "[publication](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644)"
    link2 = "[publication](https://www.sciencedirect.com/science/article/pii/S2213158216300869)"

    if sss['language'] == "fr":
        st.header("Publications Scientifiques", anchor='publications', divider="orange")
        st.markdown(f"""
        * Golos M & al. (2015), *Multistabilité dans des modèles d'activité cérébrale à grande échelle*, PLOS Computational Biology 
            ({link1})
        * Wirsich J & al. (2016), *Les mesures analytiques du cerveau entier de la communication en réseau révèlent
        une corrélation structure-fonction accrue dans l'épilepsie du lobe temporal droit*, Elsevier 
            ({link2})
        """)

    elif sss['language'] == "en":
        st.header("Scientific Publications", anchor='publications', divider="orange")
        st.markdown(f"""
        * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology 
            ({link1})
        * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier 
            ({link2})
        """)

if __name__ == "__main__":
    utils.always()
    main()
