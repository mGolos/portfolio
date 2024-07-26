import streamlit as st
from tools import utils
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("A propos de moi", anchor='about', divider="orange")
        st.markdown("""
            > Bonjour, je m'appelle Mathieu Golos.  
            
            > Polyvalent avec un profil orienté vers la **science** et la **programmation**, je suis un travailleur altruiste et créatif.
            > J'aime mon autonomie mais je m'épanouis au sein d'une équipe avec laquelle il est primordial pour moi de créer des liens.  
            
            > J'ai toujours eu un vif intérêt pour les disciplines scientifiques et l'ai satisfait par une formation pluridisciplinaire qui m'a conduit à un master spécialisé en Modélisation et Calcul Scientifiques.
            > Formé au calcul intensif, j'ai effectué une thèse enrichissante en neurosciences computationnelles, travaillant sur les réseaux de neurones, l'apprentissage automatique et les séries temporelles.  
            
            > Après un stage en tant qu'ingénieur Machine Learning, j'ai travaillé comme Expert en Science des données chez XRator qui aborde les risques cyber de manière préventive, et chez Jagger&Lewis pour prédire les comportements de chiens à partir d'activités temporelles.
            > Je cherche actuellement à en apprendre davantage dans certains domaines au cours de la prochaine décennie pour un projet à long terme.
        """)
        st.info("Recherche un poste en distanciel")
    
    elif sss['language'] == "en":
        st.header("About me", anchor='about', divider="orange")
        st.markdown("""
            > Hello, my name is Mathieu Golos.  
            
            > Versatile with a profile oriented towards science and programming, I am an altruistic and creative worker.
            > I like my autonomy but I flourish within a team with which it is essential for me to create links.  
            
            > I always had a keen interest in scientific disciplines and satisfied this with multidisciplinary training which led me to a master's degree specializing in Scientific Modeling and Computing.
            > Trained in Intensive Computing, I did an enriching thesis in Computational Neurosciences, working on Neural Networks, Machine Learning and Time Series.  

            > After an internship as a Machine Learning engineer, I worked as a Data Scientist at XRator which approaches cyber risks in a preventive way, and Jagger&Lewis to predict dogs' behaviors from temporal activities.
            > I am currently looking to learn more in certain areas over the next decade for a long-term project.
        """)
        st.info("Searching for a remote position")
    
    st.image('images/photo1.jpg')


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
