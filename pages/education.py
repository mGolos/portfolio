import utils
import streamlit as st
sss = st.session_state


def main():
    sup = "[Centrale Supelec](https://www.centralesupelec.fr/)"
    amu = "[AMU](https://ecole-doctorale-463.univ-amu.fr/fr)"
    rennes = "[Rennes1](https://www.univ-rennes.fr/)"
    lille = "[Lille1](https://www.univ-lille.fr/)"
    iut = "[UPHF](https://www.uphf.fr/iut/presentation/departement-formations/mesures-physiques)"
    
    header = st.empty()
    st.warning("En cours d'édition" if sss['language'] == "fr" else "Ongoing modifications")
    d_lines = {}
    edu_tags = ['amu', 'sup', 'rennes', 'lille', 'iut']
    edu_names = ['AMU', 'Supelec', 'Rennes1', 'Lille1', 'UPHF']
    
    
    # Tabs or Containers
    if sss['layout'] == "wide":
        containers = st.tabs(edu_names)
    else:
        containers = [st.container() for _ in edu_names]
    
    for container, edu_name in zip(containers, edu_tags):
        img, txt = container.columns((1,5))
        container.write('---')
        img.image(sss['images'][edu_name])
        d_lines[edu_name] = txt.empty(), txt.empty(), txt.empty()
    

    if sss['language'] == "fr":
        header.header("Éducation", anchor='education', divider="orange")
        
        d_lines['amu'][0].write(f"#### Thèse en Neurosciences Computationnelles, {amu}")
        d_lines['amu'][1].markdown("""
            *2013* / **Marseille**  
            A l'école doctorale Sciences du Mouvement Humain
            * Multistabilité dans la modélisation de l’activité cérébrale à large échelle
            * Etude de modèles neuro-dynamiques pour la reconnaissance de configurations d'activité à l'état de repos (Resting-State Networks)
        """)
        d_lines['amu'][2].expander('Matières').write("""
            En cours...
        """)
        
        d_lines['sup'][0].write(f"#### Master Ingénieur Machine Learning, {sup}")
        d_lines['sup'][1].markdown("""
            *2021* / **Paris**  
            En collaboration avec OpenClassrooms
        """)
        d_lines['sup'][2].expander('Matières').write("""
            En cours...
        """)
        
        d_lines['rennes'][0].write(f"#### Master Modélisation et Calculs Scientifiques, {rennes}")
        d_lines['rennes'][1].markdown("""
            *2012* / **Rennes**  
        """)
        d_lines['rennes'][2].expander('Matières').write("""
            En cours...
        """)
        
        d_lines['lille'][0].write(f"#### Licence Physique Fondamentale, {lille}")
        d_lines['lille'][1].markdown("""
            *2010* / **Lille**  
        """)
        d_lines['lille'][2].expander('Matières').write("""
            En cours...
        """)
        
        d_lines['iut'][0].write(f"#### DUT Mesures Physiques - Génie des matériaux, {iut}")
        d_lines['iut'][1].markdown("""
            *2008* / **Valenciennes**  
        """)
        d_lines['iut'][2].expander('Matières').write("""
            En cours...
        """)
    

    elif sss['language'] == "en":
        header.header("Education", anchor='education', divider="orange")
        
        d_lines['amu'][0].write(f"#### PhD in Computational Neurosciences, {amu}")
        d_lines['amu'][1].markdown("""
            *2013* / **Marseille**  
            In the doctoral school "Sciences du Mouvement Humain"
            * Multistability in large scale of brain activity modeling
            * Study of neuro-dynamic models for the recognition of activity configurations in the resting state (Resting-State Networks)
        """)
        d_lines['amu'][2].expander('Subjects').write("""
            Ongoing...
        """)
        
        d_lines['sup'][0].write(f"#### Master Ingénieur Machine Learning, {sup}")
        d_lines['sup'][1].markdown("""
            *2021* / **Paris, France**  
            In collaboration with OpenClassrooms
        """)
        d_lines['sup'][2].expander('Subjects').write("""
            Ongoing...
        """)
        
        d_lines['rennes'][0].write(f"#### Master degree in Modeling and Scientists Calculus, {rennes}")
        d_lines['rennes'][1].markdown("""
            *2012* / **Rennes, France**  
        """)
        d_lines['rennes'][2].expander('Subjects').write("""
            Ongoing...
        """)
        
        d_lines['lille'][0].write(f"#### Degree in Fundamental Physics, {lille}")
        d_lines['lille'][1].markdown("""
            *2010* / **Lille, France**  
        """)
        d_lines['lille'][2].expander('Subjects').write("""
            Ongoing...
        """)
        
        d_lines['iut'][0].write(f"#### Technical degree in Physical Measurements - Material Engineering, {iut}")
        d_lines['iut'][1].markdown("""
            *2008* / **Valenciennes, France**  
        """)
        d_lines['iut'][2].expander('Subjects').write("""
            Ongoing...
        """)


if __name__ == "__main__":
    utils.always()
    main()
