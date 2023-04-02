import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from utils import st_query_radio


def apropos(language="fr"):
    if language == "fr":
        st.markdown("""
            ## Bonjour et bienvenue !
            ---
            # Mathieu Golos
            > Polyvalent avec un profil orienté vers les sciences et la programmation, je suis un travailleur altruiste et créatif.
            > Autonome, je m'épanouis pleinement au sein d'une équipe avec laquelle il m'est indispensable de créer des liens.
            
            > J’ai toujours voué un vif intérêt aux disciplines scientifiques et satisfait celui-ci par des formations pluridisciplinaires qui m’ont amené vers un master spécialisé dans la Modélisation et les Calculs Scientifiques.
            > Formé sur les Calculs Intensifs, j'ai fait une thèse enrichissante en Neurosciences Computationnelles, en travaillant sur des Réseaux Neuronaux et l'Apprentissage Automatique.
            
            > Après un stage en tant qu'ingénieur en Apprentissage Automatique, j'ai travaillé en tant qu'Expert en Science des données chez XRator qui approche les cyber-risques de manière préventive.
            > Je cherche actuellement à apprendre toujours plus dans certains domaines au cours de la prochaine décennie pour un projet sur le long terme.
        """)
    elif language == "en":
        st.markdown("""
            ## Hello and welcome!
            ---
            # Mathieu Golos
            > Versatile with a profile oriented towards science and programming, I am an altruistic and creative worker.
            > I like my autonomy but I flourish within a team with which it is essential for me to create links.  

            > I always had a keen interest in scientific disciplines and satisfied this with multidisciplinary training which led me to a master's degree specializing in Scientific Modeling and Computing.
            > Trained in Intensive Computing, I did an enriching thesis in Computational Neurosciences, working on Neural Networks and Machine Learning.  
            
            > After an internship as a Machine Learning engineer, I worked as a Data Scientist at XRator which approaches cyber risks in a preventive way.
            > I am currently looking to learn more in certain areas over the next decade for a long-term project.
        """)
    st.markdown("""
        ---
        <img src="https://drive.google.com/uc?export=view&id=1W3Bax_Fkwl4zKR4DCY_GLWXJ20qkcxxT" alt="drawing" width="100%"/>
        """,
        unsafe_allow_html =True)
    
    
def parcours(language="fr"):
    xrator = "[XRator](https://www.x-rator.com/)"
    lindera = "[Lindera](https://www.lindera.de/)"
    
    if language == "fr":
        st.markdown(f"""
            # Expériences
            * `[2023] (2 mois)` - **Scientifique de la donnée Clinique**, {lindera} *(France/Vietnam/Allemagne)*
            * `[2022] (9 mois)` - **Scientifique de la donnée**, {xrator} *(France/Vietnam)*
            * `[2021] (8 mois)` - **Stage Ingénieur Machine Learning**, OpenClassrooms *(Lille)*
            * `[2019 - 2020] (7 mois)` - **Ingénieur DevOps**, Alpha Conseils *(St-Germain-en-Laye)*
            * `[2013 - 2017] (4 ans)` - **Doctorant en Neurosciences Computationnelles**, INS/INSERM 1106 *(Marseille)*
            * `[2013] (9 mois)` - **Assistant Ingénieur**, INS, INSERM 1106 *(Marseille)*
            
            # Formations
            * `[2021]` - **Master Ingénieur Machine Learning**, Centrale Supélec *(Paris)*
            * `[2012]` - **Master Modélisation et Calculs Scientifiques**, Rennes1 *(Rennes)*
            * `[2010]` - **Licence Physique Fondamentale**, Lille1 *(Lille)*
            * `[2008]` - **DUT Mesures Physiques - Génie des matériaux** *(Valenciennes)*
        """)
    elif language == "en":
        st.markdown(f"""
            # Experiences
            * `[2023] (2 mois)` - **Data Scientist Clinical**, {lindera} *(France/Vietnam/Germany)*
            * `[2022] (9 months)` - **Data Scientist**, {xrator} *(France/Vietnam)*
            * `[2021] (8 months)` - **Machine Learning Engineer (Internship)**, OpenClassrooms *(Lille)*
            * `[2019 - 2020] (7 months)` - **DevOps Engineer**, Alpha Conseils *(St-Germain-en-Laye)*
            * `[2013 - 2017] (4 years)` - **PhD Candidate in Computational Neurosciences**, INS/INSERM 1106 *(Marseille)*
            * `[2013] (9 months)` - **Assistant Engineer**, INS, INSERM 1106 *(Marseille)*
            
            # Education
            * `[2021]` - **Master degree in Machine Learning Engineer**, Centrale Supélec *(Paris)*
            * `[2012]` - **Master degree in Modeling and Scientists Calculus**, Rennes1 *(Rennes)*
            * `[2010]` - **Degree in Fundamental Physics**, Lille1 *(Lille)*
            * `[2008]` - **Technical degree in Physical Measurements - Material Engineering** *(Valenciennes)*
        """)
        
    
def projets(language="fr"):
    streamlit = "[Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)"
    link1 = "[Notebooks](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/question_tagging)"
    link2 = f"[!{streamlit}](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=question-tagging)"
    link3 = "[Notebooks](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/breed_classifier)"
    link4 = f"[!{streamlit}](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=breed-classifier)"
    
    if language == "fr":
        st.markdown(f"""
            # Projets
            * Question Tagging ({link1}, {link2}) :  
                Production d'une application pour l'automatisation d'étiquetage multiple de questions en utilisant les algorithmes les plus récents/performants.  
                `[ État de l'art / NLP / XMC / Deep Learning ]`
            ---
            * Breed Classifier ({link3}, {link4}) :  
                Production d'une application de reconnaissance de race d'images de chiens.  
                `[ Deep Learning / Transfert Learning ]`
            ---
            * Segmentation de clients d'un site e-commerce.  
                `[ k-means / HCA / DBSCAN ]`
            ---
            * Anticipation de la consommation électrique et émissions CO² d'une ville.  
                `[ SVM / Forêt aléatoires / Boosting ]`
            ---
            * Conception d'une application sur des données nutritionnelles.  
            ---
            (Nettoyage en cours)
            """)
    elif language == "en":
        st.markdown(f"""
            # Projects
            * Question Tagging ({link1}, {link2}):  
                Produce an application for automatic multi-tagging of questions using state of the art algorithms.  
                `[ SOTA / NLP / XMC / Deep Learning ]`
            ---
            * Breed Classifier ({link3}, {link4}):               
                Produce an application for race recognition of dog images.  
                `[ Deep Learning / Transfert Learning ]`
            ---
            * Segmenting customers of an e-commerce website.  
                `[ k-means / HCA / DBSCAN ]`
            ---
            * Anticipating a city's electricity consumption and CO² emissions.  
                `[ SVM / Random Forest / Boosting ]`
            ---
            * Design of an application on nutritional data for public health.  
            ---
            (Cleaning in progress)
            """)


def publications(language="fr"):
    if language == "fr":
        st.markdown("# Publications Scientifiques")
    elif language == "en":
        st.markdown("# Scientific Publications")
        
    st.markdown("""
        * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology 
            ([publication](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644))
        * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier 
            ([publication](https://www.sciencedirect.com/science/article/pii/S2213158216300869))
        """)


def iframe(src:str):
    return components.iframe(src=src, width=None, height=1020, scrolling=True)
    
    
def cv(language="fr"):
    url_fr = "https://1drv.ms/b/s!Ah3jei6FBtQIhOx0zmTSlEkxKYQh4Q?e=sXRqdm"
    url_en = "https://1drv.ms/b/s!Ah3jei6FBtQIhOx1BI-_YOe1orF8Qg?e=X00EOb"
    src_fr = "https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2179476&authkey=AJw1dkWCCYWhFE4&em=2"
    src_en = "https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2179477&authkey=AD16Jnht-e2tXmY&em=2"
    if language == "fr":
        st.markdown(f"Télécharger la version [française]({url_fr}) | [anglaise]({url_en})")
        iframe(src_fr)
    elif language == "en":
        st.markdown(f"Download the [english version]({url_en}) | [french version]({url_fr})")
        iframe(src_en)

        
def recommandation(language="fr"):
    if language == "fr":
#         tab1, tab2 = st.tabs(["INS (En)", "XRator"])
        tab1, tab2 = st.tabs(["Institut de Neurosciences des Systèmes (Traduit)", "..."])
        with tab1:
            iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2178515&authkey=AD4gq0CU3sAJEnk&em=2")
#         with tab2:
#             st.markdown("Soon...")
    elif language == "en":
        tab1, tab2 = st.tabs(["Institut de Neurosciences des Systèmes", "..."])
        with tab1:
            iframe("https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2149593&authkey=AGqw88JCpvqX2_Q&em=2")
#         with tab2:
#             st.markdown("Soon...")
    
    
def contact(language="fr"):
    if language == "fr":
        st.markdown('''
            # Contactez-moi
            > La meilleur façon de me joindre est par email.  
            > Cependant, je liste ici les différents moyens de me joindre.
            > N'hésitez pas à me contacter sur l'un d'entre eux !
            ''')
    elif language == "en":
        st.markdown('''
            # Contact
            > The best way to contact me is by email.  
            > However, I list here the different methods.
            > Feel free to contact me on any of them !
            ''')
        
    st.markdown('''
        ---
        [![](https://img.icons8.com/officel/48/000000/email.png)mathieu.golos@gmail.com](mail:mathieu.golos@gmail.com)  
        [![](https://img.icons8.com/fluent/48/000000/phone.png):flag-fr: +336 11 47 89 01](tel:+33611478901)  
        [![](https://img.icons8.com/fluent/48/000000/phone.png):flag-vn: +847 95 59 49 42](tel:+84795594942)  
        [![](https://img.icons8.com/color/48/000000/linkedin.png)LinkedIn](https://www.linkedin.com/in/mathieu-golos-25055b77/)  
        [![](https://img.icons8.com/dusk/48/000000/worldwide-location.png)Lille (FRANCE)](https://goo.gl/maps/eXC8BJh9qGXWBgZDA)  
        ''')


def main():
    language = st.sidebar.radio('', ['English', 'Français'])
    functions = apropos, parcours, projets, publications, cv, recommandation, contact
    names_fr = "A propos", "Parcours", "Projets", "Publications", "Curriculum vitae", "Recommandations", "Contactez-moi"
    names_en = "About", "Journey", "Projects", "Publications", "Curriculum vitae", "Recommendations", "Contact"
    
    if language == 'Français':
        st_query_radio("Navigation", "p", {k:v for k,v in zip(names_fr, functions)})(language="fr")
        
    elif language == 'English':
        st_query_radio("Navigation", "p", {k:v for k,v in zip(names_en, functions)})(language="en")
    
    
if __name__ == "__main__":
    st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="auto",
        page_icon=None,
        layout="centered"
    )
    st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    st.sidebar.image('hands.png', width=200)
    with open('.streamlit/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    main()
