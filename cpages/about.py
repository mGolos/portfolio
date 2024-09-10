import streamlit as st
from tools import utils
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("A propos de moi", anchor='about', divider="orange")
        st.markdown("""
            > Bonjour, je m'appelle Mathieu Golos.  
            
            > Polyvalent avec un profil orienté vers la **science** et la **programmation**, je suis un travailleur altruiste et créatif.
            > J'ai toujours eu un vif intérêt pour les disciplines scientifiques et l'ai satisfait par une **formation pluridisciplinaire**.
            > Une thèse enrichissante en **neurosciences computationnelles** m'a amené à travailler sur l'**Apprentissage Automatique** et les **Séries temporelles**.  
            
            > J'ai pu m'investir par la suite dans la **cyber prévention**, le **biomédical** ou le **bien-être canin**, et je cherche toujours de nouveaux projets captivants.
            > **Autonome** mais je m'épanouis au sein d'une équipe avec laquelle il est primordial pour moi de **créer des liens**.  
            
            > Ouvert à toute proposition et tout type de contrat.
        """)
    
    elif sss['language'] == "en":
        st.header("About me", anchor='about', divider="orange")
        st.markdown("""
            > Hello, my name is Mathieu Golos.  
            
            > Versatile with a profile oriented towards **science** and **programming**, I am an altruistic and creative worker.
            > I always had a keen interest in scientific disciplines and satisfied this with **multidisciplinary training**.
            > An enriching thesis in **Computational Neurosciences**, led me working on **Machine Learning** and **Time Series**.  
            
            > I could invest myself in **cyber prevention**, **biomedical**, or **canine well-being**, and I'm always looking for new captivating projects.
            > **Independent**, but I thrive within a team with whom it's essential for me to **build relationships**.
            
            > Open to all proposals and any type of contract.
        """)
    
    st.image('images/photo1.jpg')


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
