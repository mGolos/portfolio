import utils
import streamlit as st
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.markdown("# Publications Scientifiques")
    elif sss['language'] == "en":
        st.markdown("# Scientific Publications")
        
    st.markdown("""
        * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology 
            ([publication](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644))
        * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier 
            ([publication](https://www.sciencedirect.com/science/article/pii/S2213158216300869))
        """)


if __name__ == "__main__":
    utils.always()
    main()
