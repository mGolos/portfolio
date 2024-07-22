import utils
import streamlit as st
sss = st.session_state


def main():
    sup = "[Centrale Supelec](https://www.centralesupelec.fr/)"
    rennes = "[Rennes1](https://www.univ-rennes.fr/)"
    lille = "[Lille1](https://www.univ-lille.fr/)"
    iut = "[UPHF](https://www.uphf.fr/iut/presentation/departement-formations/mesures-physiques)"
    
    header = st.empty()
    st.warning("En cours d'édition" if sss['language'] == "fr" else "Ongoing modifications")
    d_lines = {}
    for job in ['sup', 'rennes', 'lille', 'iut']:
        img, txt = st.columns((1,5))
        st.write('---')
        img.image(sss['images'][job])
        d_lines[job] = txt.empty(), txt.empty(), txt.empty()
    

    if sss['language'] == "fr":
        header.header("Éducation", anchor='education', divider="orange")
        
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
