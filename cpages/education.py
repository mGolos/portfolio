import streamlit as st
from tools import utils
sss = st.session_state


def main():
    sup = "[Centrale Supelec](https://www.centralesupelec.fr/)"
    amu = "[AMU](https://ecole-doctorale-463.univ-amu.fr/fr)"
    rennes = "[Rennes1](https://www.univ-rennes.fr/)"
    lille = "[Lille1](https://www.univ-lille.fr/)"
    iut = "[UPHF](https://www.uphf.fr/iut/presentation/departement-formations/mesures-physiques)"
    edu = "[EduGroupe](https://edugroupe.com/ingenieur-devops/)"
    
    header = st.empty()
    d_lines = {}
    tags = ['sup', 'edu', 'amu', 'rennes', 'lille', 'iut']
    names = ['Supelec', 'EduGroupe', 'AMU', 'Rennes1', 'Lille1', 'UPHF']
    
    dico = {
        "sup": {
            "title": (
                f"Master Machine Learning Engineer, {sup}",
                f"Master Ingénieur Machine Learning, {sup}"),
            "dateplace": (
                "*2021* / **Paris, France**",
                "*2021* / **Paris**"),
            "description": (
                "API, Data cleaning/exploration, Algorithmics, Natural Language Processing, Feature engineering, Computer Vision, Imputation, Regression, Classification, Communication, Optimization, Extreme multi-tagging, State of the art, Image processing, Neural network, Transfer learning",
                "API, Nettoyage/Exploration de données, Algorithmie, Traitement automatique du language, Ingénierie des caractéristiques, Computer Vision, Imputation, Regression, Classification, Communication, Optimisation, Multi-étiquetage extrême, État de l'art, Traitement d'image, Réseaux neuronaux, Apprentissage par transfert"),
        },
        "edu": {
            "title": (
                f"DevOps Engineer Training, {edu}",
                f"Formation Ingénieur DevOps, {edu}"),
            "dateplace": (
                "*2019* / **Paris, France**",
                "*2019* / **Paris**"),
            "description": (
                "Shell Programming, Advanced Linux Server Administration, Python, Database Administration, Server Administration, Nagios, Git, Elasticsearch, Docker, Puppet, Jenkins, Ansible, Agile Scrum Methodology",
                "Programmation Shell, Administration Linux avancée, Python, Base de données, Administration du serveur, Nagios, Git, Elasticsearch, Docker, Puppet, Jenkins, Ansible, Méthode Agile Scrum"),
        },
        "amu": {
            "title": (
                f"PhD in Computational Neurosciences, {amu}",
                f"Thèse en Neurosciences Computationnelles, {amu}"),
            "dateplace": (
                "*2013* / **Marseille (France)**",
                "*2013* / **Marseille**"),
            "description": (
                "Temporal multistability, Dynamical systems, Cellular automata, Mathematical modeling, Statistics, Machine learning, Classification, Neuro-dynamics, Pattern recognition, Resting-State networks, Medical imaging, State of the art, Multi-threading, Epilepsy", 
                "Multistabilité temporelle, Systèmes dynamiques, Automates cellulaires, Modélisation mathématique, Statistiques, Apprentissage automatique, Classification, Dynamique neuronale, Reconnaissance d'activité, Réseaux d'activité en état de repos, Imagerie médicale, État de l'art, Traitement en parallèle, Épilepsie"),
        },
        "rennes": {
            "title": (
                f"Master degree in Modeling and Scientists Calculus, {rennes}",
                f"Master Modélisation et Calculs Scientifiques, {rennes}"),
            "dateplace": (
                "*2012* / **Rennes, France**",
                "*2012* / **Rennes**"),
            "description": (
                "Methods and tools for numerical simulation, Medical imaging, Simulation, Modeling, Programming (C++/F90), High performance computing, Biomechanics, Inverse problems, Geophysics, Fluid-structure interactions, Multiphysics, Physics of granular environments, Mechanics",
                "Méthodes et outils à la simulation numérique, Imagerie médicale, Simulation, Modélisation, Programmation (C++/F90), Calculs intensifs, Biomécanique, Problèmes inverses, Géophysique, Intéractions fluide-structure, Multiphysique, Physique des milieux granulaires, Mécanique"),
        },
        "lille": {
            "title": (
                f"Bachelor's degree in Fundamental Physics, {lille}",
                f"Licence Physique Fondamentale, {lille}"),
            "dateplace": (
                "*2010* / **Lille, France**",
                "*2010* / **Lille**"),
            "description": (
                "Quantum mechanics, Electromagnetism, Tools for physics, Numerical simulation, Analytical mechanics, Thermodynamics, Optics, Wave and vibration, Properties of materials, Physics and statistics, Astrophysics, Earth and environmental physics",
                "Mécanique quantique, Électromagnétisme, Outils pour la physique, Simulation numérique, Mécanique analytique, Thermodynamique, Optique, Onde et vibration, Propriétés de la matière, Physique et statistiques, Astrophysique, Physique de la Terre et de l'environnement"),
        },
        "iut": {
            "title": (
                f"Technical degree in Physical Measurements - Materials Engineering, {iut}",
                f"DUT Mesures Physiques - Génie des matériaux, {iut}"),
            "dateplace": (
                "*2008* / **Valenciennes, France**",
                "*2008* / **Valenciennes**"),
            "description": (
                "Mathematics, Computer science, Programming, Signal processing, Metrology, Instrumentation electronics, Chemical analysis techniques, Thermodynamics, Material structure and properties, Optics, Fluid mechanics, Mechanics",
                "Mathématiques, Informatique, Programmation, Traitement du signal, Métrologie, Electronique d'instrumentation, Techniques d'analyse chimique, Thermodynamique, Structure et propriétés des matériaux, Optique, Mécanique des fluides, Mécanique"),
        },
    }
    
    
    # Tabs or Containers
    if sss['layout'] == "wide":
        containers = st.tabs(names)
        
        for container, tag in zip(containers, tags):
            img, title = container.columns((1,4), vertical_alignment='center')
            img.image(sss['images'][tag], width=int(0.3 * sss['layout_width']))
            d_lines[tag] = title, container.empty(), container.empty()
    else:
        tabs = st.tabs([
            'Date / Lieu' if sss["lg_key"] else 'Date / Place',
            'Matières' if sss["lg_key"] else 'Subjects'
        ])
        containers = [[tab.container() for _ in names] for tab in tabs]
        
        for itab, tab in enumerate(tabs):
            d_lines[itab] = {}
            for container, tag in zip(containers[itab], tags):
                img, txt = container.columns((1,7))
                img.image(sss['images'][tag])
                d_lines[itab][tag] = txt.empty(), txt.empty()
    
    # Content
    header.header(
        "Éducation" if sss["lg_key"] else 'Education', 
        anchor='education', divider="orange")
    
    if sss['layout'] == 'wide':
        for tag, cont in d_lines.items():
            e = dico[tag]
            cont[0].write('#### ' + e['title'][sss["lg_key"]])
        
            cont[1].markdown(e['dateplace'][sss["lg_key"]])
            with cont[2].expander('Matières' if sss["lg_key"] else 'Subjects', expanded=True):
                st.markdown('`'+ e['description'][sss["lg_key"]].replace(', ', '` · `') + '`')
    else:
        for itab, tab in enumerate(tabs):
            for tag, cont in d_lines[itab].items():
                e = dico[tag]
                cont[0].write('#### ' + e['title'][sss["lg_key"]])
                if itab == 0:
                    cont[1].markdown(e['dateplace'][sss["lg_key"]])
                elif itab == 1:
                    cont[1].markdown('`'+ e['description'][sss["lg_key"]].replace(', ', '` · `') + '`')


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
