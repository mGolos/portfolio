import streamlit as st
from streamlit_image_comparison import image_comparison
from tools import utils
sss = st.session_state


def main():
    if sss['language'] == "fr":
        st.header("A propos de moi", anchor='about', divider="orange")
        st.markdown("""
            📊 Data Scientist | 🤖 AI Engineer | 💡 Problem Solver
            > Curieux et polyvalent, j'évolue à l'intersection de la science, de la programmation et de l'innovation.
            Avec mon expérience en Neurosciences Computationnelles, je me spécialise en Machine Learning et en analyse de séries temporelles, avec des applications variées allant de la cybersécurité et du biomédical au bien-être canin.

            > Ce que je peux apporter :  
            ✔ Expertise multidisciplinaire en science et en programmation  
            ✔ Expérience en IA, science des données & modélisation prédictive  
            ✔ Passion pour les projets à fort impact  
            ✔ Autonomie et esprit d'équipe

            > Toujours en quête de nouveaux défis et collaborations passionnantes — échangeons !
        """)
    
    elif sss['language'] == "en":
        st.header("About me", anchor='about', divider="orange")
        st.markdown("""
            📊 Data Scientist | 🤖 AI Engineer | 💡 Problem Solver
            > Versatile and driven by curiosity, I thrive at the intersection of science, programming, and innovation. With an experience in Computational Neuroscience, I specialize in Machine Learning and Time Series Analysis, applying my expertise to diverse fields — from cybersecurity and biomedical research to canine well-being.

            > What I can bring:  
            ✔ Multidisciplinary expertise in science & programming  
            ✔ Experience in AI, data science & predictive modeling  
            ✔ Passion for meaningful, high-impact projects  
            ✔ A balance of independence & team collaboration

            > Always open to new challenges, collaborations, and opportunities — let's connect!
        """)
    
    # st.audio(f"audio/presentation_{sss['language']}.mp3")
    # st.image('images/photo1.jpg')
    image_comparison(
        img1=utils.load_image("images/photo1b.jpg"),
        img2=utils.load_image("images/photo1.jpg"),
        label1="Style Transfer",
        label2="Original",
        # width=1920,
        starting_position=70,
        show_labels=True,
        make_responsive=True,
        in_memory=True,
    )


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
