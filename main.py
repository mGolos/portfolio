import streamlit as st
from pathlib import Path
from utils import st_query_radio


def apropos():
    st.markdown((Path(__file__).parents[0]/"README.md").read_text(encoding="utf-8"))
    
    
def parcours():
    st.markdown("""
        # Expériences
        * [2021] (8 mois) - **Stage Ingénieur Machine Learning**, OpenClassrooms** *(Lille)*
        * [2019 - 2020] (7 mois) - **Ingénieur DevOps**, Alpha Conseils *(St-Germain-en-Laye)*
        * [2013 - 2017] (4 ans) - **Doctorant en Neurosciences Computationnelles**, INS/INSERM 1106 *(Marseille)*
        * [2013] (9 mois) - **Assistant Ingénieur**, INS, INSERM 1106 *(Marseille)*
        
        # Formations
        * [2021] - **Master Ingénieur Machine Learning**, Centrale Supélec *(Paris)*
        * [2012] - **Master Modélisation et Calculs Scientifiques**, Rennes1 *(Rennes)*
        * [2010] - **Licence Physique Fondamentale**, Lille1 *(Lille)*
        * [2008] - **DUT Mesures Physiques - Génie des matériaux** *(Valenciennes)*
    """)
    
    
def projets():
    st.markdown("""
        # Projets
        * [Question Tagging](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/question_tagging) :
          [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=question-tagging)  
            Production d'une application pour l'automatisation d'étiquetage multiple de questions en utilisant les algorithmes les plus récents/performants.  
            **[ État de l'art / NLP / XMC / Deep Learning ]**
            
        * [Breed Classifier](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/breed_classifier) :
          [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=breed-classifier)  
            Production d'une application de reconnaissance de race d'images de chiens  
            **[ Deep Learning / Transfert Learning ]**
            
        * Segmentation de clients d'un site e-commerce  
            **[ k-means / HCA / DBSCAN ]**
            
        * Anticipation de la consommation électrique et émissions CO² d'une ville  
            **[ SVM, Forêt aléatoires, Boosting ]**
            
        * Conception d'une application sur des données nutritionnelles  
        
        (Nettoyage en cours)
        """)
    
    
def publications():
    st.markdown("""
        # Publications Scientifiques
        * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology ([lien]
            (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644))
        * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier ([lien]
            (https://www.sciencedirect.com/science/article/pii/S2213158216300869))
        """)
    
    
def cv():
    st.markdown(
        "[Télécharger la version française](https://1drv.ms/b/s!Ah3jei6FBtQIhMJLGYXpU8wBcYAe_w)")
    st.markdown(
        '''<iframe src="https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2174059&authkey=AJ_U266yaU04KXk&em=2"*
        width="750" height="1060" frameborder="0" scrolling="no"></iframe>''',
        unsafe_allow_html =True)

    
def contact():
    st.markdown('''
        # Contactez-moi
        > La meilleur façon de me joindre est par mail.  
        Cependant, je liste ici les autres moyens de me joindre.  
        N'hésitez pas à me contacter sur l'un d'entre eux !
        
        [![](https://img.icons8.com/fluent/48/000000/phone.png)+336 11 47 89 01](tel:+33611478901)  
        [![](https://img.icons8.com/officel/48/000000/email.png)mathieu.golos@gmail.com](mail:mathieu.golos@gmail.com)  
        [![](https://img.icons8.com/color/48/000000/linkedin.png)LinkedIn](https://www.linkedin.com/in/mathieu-golos-25055b77/)  
        [![](https://img.icons8.com/bubbles/50/000000/github.png)GitHub](https://github.com/mGolos)
        ''')


def main():
    st_query_radio("Navigation", "p", {
        "A propos": apropos,
        "Parcours": parcours,
        "Projets": projets,
        "Publications": publications,
        "Curriculum vitae": cv,
        "Contactez-moi": contact,
    })()


if __name__ == "__main__":
    st.set_page_config(
        page_title='Golos',
        initial_sidebar_state="auto",
        page_icon=None,
        layout="centered"
    )
    st.sidebar.image('hands.png')
    with open('.streamlit/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    main()
