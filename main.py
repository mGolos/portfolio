import streamlit as st
from pathlib import Path
from utils import st_query_radio


def apropos(language="fr"):
    if language == "fr":
        st.markdown("""
            ## Bonjour et bienvenue sur mon portfolio !
            ---
            # Mathieu Golos
            > Polyvalent avec un profil orienté vers les sciences et la programmation, je suis un travailleur altruiste et créatif.
            J'aime l'autonomie et m'épanouir au sein d'une équipe avec laquelle il m'est indispensable de créer des liens.  

            > J’ai toujours voué un vif intérêt aux disciplines scientifiques et satisfait celui-ci par des formations pluridisciplinaires 
            qui m’ont amené vers un master spécialisé dans la Modélisation et les Calculs Scientifiques. 
            Formé sur les Calculs Intensifs, j'ai fait une thèse enrichissante en Neurosciences Computationnelles, 
            en travaillant sur des Réseaux Neuronaux et l'Apprentissage Automatique.  

            > J'ai récemment fini un stage en tant qu'ingénieur en Apprentissage Automatique
            et je cherche actuellement à aller de l'avant dans plusieurs de ses domaines au cours de la prochaine décennie.
        """)
    elif language == "en":
        st.markdown("""
            ## Hello and welcome on my portfolio !
            ---
            # Mathieu Golos
            > Versatile with a profile oriented towards science and programming, I am an altruistic and creative worker.
            I like my autonomy, but I flourish within a team with which it is essential for me to create links.

            > I always had a keen interest in scientific disciplines and satisfied this with multidisciplinary
            training which led me to a master's degree specializing in Scientific Modeling and Computing. 
            Trained in Intensive Computing, I did an enriching thesis in Computational Neurosciences, working on Neural Networks and Machine Learning.
            
            > I recently completed an internship as a Machine Learning Engineer and 
            am currently looking to move forward in several of its areas over the next decade.
        """)
    st.markdown("""
        ---
        <img src="https://drive.google.com/uc?export=view&id=1W3Bax_Fkwl4zKR4DCY_GLWXJ20qkcxxT" alt="drawing" width="700"/>
        """,
        unsafe_allow_html =True)
        
    
    
def parcours(language="fr"):
    if language == "fr":
        st.markdown("""
            # Expériences
            * `[2022] (9 mois)` - **Scientifique de la donnée**, [XRator](https://www.x-rator.com/) *(France/Vietnam)*
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
        st.markdown("""
            # Experiences
            * `[2022] (9 mois)` - **Data Scientist**, [XRator](https://www.x-rator.com/) *(France/Vietnam)*
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
    if language == "fr":
        st.markdown("""
            # Projets
            * [Question Tagging](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/question_tagging) ([![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=question-tagging)) :  
                Production d'une application pour l'automatisation d'étiquetage multiple de questions en utilisant les algorithmes les plus récents/performants.  
                `[ État de l'art / NLP / XMC / Deep Learning ]`
            ---
            * [Breed Classifier](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/breed_classifier) ([![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=breed-classifier)) :  
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
        st.markdown("""
            # Projects
            * [Question Tagging](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/question_tagging) ([![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=question-tagging)):  
                Produce an application for automatic multi-tagging of questions using state of the art algorithms.  
                `[ SOTA / NLP / XMC / Deep Learning ]`
            ---
            * [Breed Classifier](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/breed_classifier) ([![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=breed-classifier)):               
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
        * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology ([lien]
            (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644))
        * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier ([lien]
            (https://www.sciencedirect.com/science/article/pii/S2213158216300869))
        """)
    
    
def cv(language="fr"):
    if language == "fr":
        st.markdown("[Télécharger la version française](https://1drv.ms/b/s!Ah3jei6FBtQIhOUpb7Wx-3nUGQrTWQ?e=5qYyve) | "
                    "[Télécharger la version anglaise](https://1drv.ms/b/s!Ah3jei6FBtQIhOUsGOshMy3LKxTFVw?e=DeMrkI)")
        st.markdown(
            '''<iframe src="https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2178505&authkey=ACciPtwGdV60lf4&em=2"*
            width="750" height="1060" frameborder="0" scrolling="no"></iframe>''',
            unsafe_allow_html =True)
    elif language == "en":
        st.markdown("[Download the english version](https://1drv.ms/b/s!Ah3jei6FBtQIhOUsGOshMy3LKxTFVw?e=DeMrkI) | "
                    "[Download the french version](https://1drv.ms/b/s!Ah3jei6FBtQIhOUpb7Wx-3nUGQrTWQ?e=5qYyve)")
        st.markdown(
            '''<iframe src="https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2178508&authkey=APB7Ex6E01QEURo&em=2"*
            width="750" height="1060" frameborder="0" scrolling="no"></iframe>''',
            unsafe_allow_html =True)
    
    
def recommandation(language="fr"):
    tab1, tab2 = st.tabs(["INS", "XRator"])
    with tab1:
        st.markdown(
            '''<iframe src="https://onedrive.live.com/embed?cid=08D406852E7AE31D&resid=8D406852E7AE31D%2149593&authkey=AGqw88JCpvqX2_Q&em=2"*
            width="750" height="1060" frameborder="0" scrolling="no"></iframe>''',
            unsafe_allow_html =True)
    with tab2:
        st.markdown("Soon...")
        st.markdown(
            '''<iframe src=""*
            width="750" height="1060" frameborder="0" scrolling="no"></iframe>''',
            unsafe_allow_html =True)
    
    
def contact(language="fr"):
    if language == "fr":
        st.markdown('''
            # Contactez-moi
            > La meilleur façon de me joindre est par email.  
            Cependant, je liste ici les autres moyens de me joindre.  
            N'hésitez pas à me contacter sur l'un d'entre eux !
            ''')
    elif language == "en":
        st.markdown('''
            # Contact
            > The best way to contact me is by email.  
            However, I have listed few other methods below.  
            Feel free to contact me on any of them !
            ''')
        
    st.markdown('''
        ---
        [![](https://img.icons8.com/dusk/48/000000/worldwide-location.png)Lille (FRANCE)](https://goo.gl/maps/eXC8BJh9qGXWBgZDA)  
        [![](https://img.icons8.com/fluent/48/000000/phone.png)+336 11 47 89 01](tel:+33611478901)  
        [![](https://img.icons8.com/officel/48/000000/email.png)mathieu.golos@gmail.com](mail:mathieu.golos@gmail.com)  
        [![](https://img.icons8.com/color/48/000000/linkedin.png)LinkedIn](https://www.linkedin.com/in/mathieu-golos-25055b77/)  
        [![](https://img.icons8.com/bubbles/50/000000/github.png)GitHub](https://github.com/mGolos)
        ''')


def main():
    language = st.sidebar.radio('', ['English', 'Français'])
    
    if language == 'Français':
        st_query_radio("Navigation", "p", {
            "A propos": apropos,
            "Parcours": parcours,
            "Projets": projets,
            "Publications": publications,
            "Curriculum vitae": cv,
            "Recommandations": recommandation,
            "Contactez-moi": contact,
        })(language="fr")
        
    elif language == 'English':
        st_query_radio("Navigation", "p", {
            "About": apropos,
            "Journey": parcours,
            "Projects": projets,
            "Publications": publications,
            "Curriculum vitae": cv,
            "Recommendations": recommandation,
            "Contact": contact,
        })(language="en")

        
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://raw.githubusercontent.com/mGolos/portfolio/main/hands.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True)
    
    
def set_page_container_style(padding_top=0, padding_bottom=10, padding_left=1, padding_right=10):
    st.write(
        f'''
        <style>
            div.block-container{padding-top:0rem;}
            .reportview-container .sidebar-content {{
                padding-top: {padding_top}rem;
            }}
            .reportview-container .main .block-container {{
                padding-top: {padding_top}rem;
                padding-right: {padding_right}rem;
                padding-left: {padding_left}rem;
                padding-bottom: {padding_bottom}rem;
            }}
        </style>
        ''', unsafe_allow_html=True)
    
set_page_container_style()    
        
if __name__ == "__main__":
    st.set_page_config(
        page_title='Golos Mathieu',
        initial_sidebar_state="auto",
        page_icon=None,
        layout="centered"
    )
#     st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
#     add_logo()
    st.sidebar.image('hands.png')
#     with open('.streamlit/style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    main()
