import streamlit as st
from tools import utils
sss = st.session_state


def main():
    present_projects = {
        "p_ocr8": {
            "name": "Consommation",
            "title": (
                f"Predicting cryptocurrency markets",
                f"Prédiction du marché de crypto-monnaies"),
            "short": (
                """`Regression` · `Signal processing` · `SOTA` · `Kaggle`  
                Predicting cryptocurrency markets.""",
                """`Régression` · `Traitement du signal` · `État de l'art` · `Kaggle`  
                Prédiction du marché de crypto-monnaies."""),
            "description": (
                """
                Ongoing...  
                *Predicting cryptocurrency markets based on data collected from different sources*
                * State-of-the-art study
                * Signal processing
                * Feature engineering (delays, aggregations)
                * Regression (Linear, Light Gradient Boosting Machine, XGBoost)
                * Hyperparameter optimization
                * Using and contributing to other kernels
                """, """
                En cours...  
                *Prédiction du marché des crypto-monnaies à partir des données amassées par différentes sources*
                * État de l'art
                * Traitement du signal
                * Ingénierie des caractéristiques (latences, agrégations)
                * Régression (Linéaire, Light Gradient Boosting Machine, XGBoost)
                * Optimisation des hyperparamètres
                * Utilisation et contribution aux autres kernels
                """),
            "images": ['p_ocr8_1'],
        },
        "p_motor": {
            "name": "Motor",
            "title": (
                f"Motor Behaviors Generation",
                f"Génération de comportement moteurs"),
            "short": (
                """`Multi-stability` · `Simulation` · `Time Series`  
                Generation of motor behavior from neuronal models.""",
                """`Multi-stabilité` · `Simulation` · `Séries Temporelles`  
                Génération de comportement moteurs à partir de modèles neuronaux."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_motor_1'],
        },
        "p_mem": {
            "name": "Meme",
            "title": (
                f"Writing a book",
                f"Écriture d'un livre"),
            "short": (
                """`Memetique` · `Writing`  
                Writing a book on the self-portrait of a meta-meme.""",
                """`Mèmétique` · `Écriture` · `RAG` · `Streamlit`  
                Rédaction assistée d'un livre sur l'auto-portrait d'un méta-mème."""),
            "description": (
                """
                Ongoing...  
                Tell the journey of a meme in the city of the mind.
                Complete analogy of a meme-based social system to explain consciousness emergence.
                """, """
                En cours...  
                Relate les périples d'un mème dans la cité de l'esprit.
                Analogie complète d'un système social de mèmes pour expliquer l'émergence de la conscience.
                """),
            "images": [],
        },
        "p_pal": {
            "name": "Palingen",
            "title": (
                f"Development of a video game experience",
                f"Développement d'une expérience videoludique"),
            "short": (
                """`Linguistics` · `Neural Networks` · `Python` · `Esperanto`  
                Development of a video game experience.""",
                """`Linguistique` · `Réseaux Neuronaux` · `Python` · `Esperanto`  
                Développement d'une expérience videoludique."""),
            "description": (
                """
                Ongoing...  
                - Studies on fundamental linguistics and linguistic programming
                - Studies on phonology of languages, particularly Esperanto
                - Bibliographic study, creation and submission of a project: *"Attempt at a multiple approach (theory/model/practice) to a perfectly regular language on learning disorders (dyslexia/dysphasia)"*
                - Conceptualization of automated generation of scenario/code
                - Research on human behavior dynamics and motorics
                """, """
                En cours...  
                - Etudes sur la linguistique fondamentale et la programmation linguistique
                - Etudes sur la phonologie des langues, plus particulièrement l'Esperanto
                - Etude bibliographique, création et soumission d'un projet : *"Tentative d'approche multiple (théorie/modèle/pratique) d'une langue parfaitement régulière sur les troubles de l'apprentissage (dyslexie/dysphasie)"*
                - Conceptualisation de génération automatisé de scénarisation/code
                - Recherche sur la dynamique des comportements humains et moteurs
                """),
            "images": [],
        },
    }
    past_projects = {
        "p_ocr7": {
            "name": "XMC",
            "title": (
                f"Extrem Multi-Label Classification (XMC) of questions",
                f"Classification à Multiple Étiquette Extrème (XMC) de questions"),
            "short": (
                """`SOTA` · `NLP` · `XMC` · `Deep Learning` · `Streamlit`  
                Produce an application to automatically multi-tag questions using state of the art algorithms.""",
                """`État de l'art` · `NLP` · `XMC` · `Deep Learning` · `Streamlit`  
                Production d'une application pour l'automatisation d'étiquetage multiple de questions en utilisant l'état de l'art des algorithmes."""),
            "description": (
                """
                Ongoing...  
                *Developing a system to automatically tag user questions on Stack Overflow*
                * Data cleaning (NLTK) and exploration
                * Feature engineering (quantitative and qualitative)
                * Multilabel extreme classification XMC (Gaussian Naive Bayes, Decision Tree Classifier, Linear Support Vector Classification, Multilabel k-Nearest Neighbours)
                * Methods (Word Embedding, Binary Relevance, Label Powerset, Classifier Chain)
                * Hyperparameter optimization
                * Creating a personal model
                * Bibliographic study of the state-of-the-art
                * Implementing more recent models (XR-Linear, XR-Transformer)
                * Creating an API in the form of an online application (Streamlit)
                """, """
                En cours...  
                *Développer un système permettant de tagger automatiquement les questions des utilisateurs sur le site Stack Overflow*
                * Nettoyage (NLTK) et exploration des données
                * Ingénierie des caractéristiques (quantitatives et qualitatives) 
                * Classification multi-étiquette extrême XMC (Gaussian Naive Bayes, Decision Tree Classifier, Linear Support Vector Classification, Multilabel k-Nearest Neighbours)
                * Méthodes (Word Embedding, Binary Relevance, Label Powerset, Classifier Chain)
                * Optimisation des hyperparamètres
                * Création d'un modèle personnel
                * Étude bibliographique de l'état de l'art
                * Implémentation de modèles plus récents (XR-Linear, XR-Transformer)
                * Création d'API sous forme d'une application en ligne (Streamlit)
                """),
            "images": ['p_ocr7_2', 'p_ocr7_3'],
        },
        "p_ocr6": {
            "name": "Breed Classifier",
            "title": (
                f"Breed Classifier",
                f"Reconnaissance de race de chien"),
            "short": (
                """`Deep Learning` · `Transfert Learning` · `Streamlit`  
                Produce an application for race recognition of dog images using deep learning algorithms.""",
                """`Deep Learning` · `Transfert Learning` · `Streamlit`  
                Production d'une application de reconnaissance de race d'images de chiens à l'aide d'algorithmes de deep learning."""),
            "description": (
                """
                Ongoing...  
                *Using Deep Learning models for an animal association wanting to automate breed identification*
                * Image processing
                * Supervised classification with multiple classes
                * Creating or implementing existing neural networks
                * Transfer learning (MobileNetV2)
                * Hyperparameter optimization
                * Creating an API in the form of an online application (Streamlit)
                """, """
                En cours...  
                *Utilisation de modèles de Deep Learning pour une association animalière souhaitant automatiser l'identification de races*
                * Traitement d'images
                * Classification supervisée à classes multiples
                * Création ou implémentation de Réseaux Neuronaux existants
                * Apprentissage par transfert (MobileNetV2)
                * Optimisation des hyperparamètres
                * Création d'API sous forme d'une application en ligne (Streamlit)
                """),
            "images": ['p_ocr6_1', 'p_ocr6_2'],
        },
        "p_ocr4": {
            "name": "Market Segment Analysis",
            "title": (
                f"Market Segment Analysis",
                f"Analyse de marché"),
            "short": (
                """`k-means` · `HCA` · `DBSCAN` · `Unsupervised Classification`  
                Segmenting customers of an e-commerce website.""",
                """`k-means` · `HCA` · `DBSCAN` · `Classification Non-supervisée`  
                Segmentation de clients d'un site e-commerce."""),
            "description": (
                """
                Ongoing...  
                *Providing marketing teams with a segmentable client segmentation to optimize communication campaigns*
                * Merging / Cleaning multiple databases
                * Exploring data
                * Feature engineering (quantitative and qualitative)
                * Unsupervised classification (k-Means, Hierarchical Agglomerative Clustering, DBSCAN)
                * Hyperparameter optimization
                """, """
                En cours...  
                *Fournir aux équipes marketing une segmentation activable de leurs clients pour optimiser les campagnes de communication*
                * Fusion / Nettoyage de multiples bases de données
                * Exploration de données
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Classification non supervisée (k-Means, Hiérarchique agglomératif, DBSCAN)
                * Optimisation des hyperparamètres
                """),
            "images": ['p_ocr4_1',],
        },
        "p_ocr3": {
            "name": "Consommation",
            "title": (
                f"Predicting Electricity Consumption and Carbon Emissions",
                f"Prédiction de consommation électrique et émissions CO²"),
            "short": (
                """`SVM` · `Random Forest` · `Boosting` · `Imputation` · `Regression`  
                Anticipating a city's electricity consumption and CO² emissions of a city.""",
                """`SVM` · `Forêt aléatoires` · `Boosting` · `Imputation` · `Régression`  
                Anticipation de la consommation électrique et émissions CO² d'une ville."""),
            "description": (
                """
                Ongoing...  
                *Predicting electricity consumption and carbon emissions for municipal buildings in Seattle*
                * Merging / Cleaning databases
                * Exploring data
                * Feature engineering (quantitative and qualitative)
                * Imputation and Regression (Linear, SVR, Random Forest, Gradient Boosting)
                """, """
                En cours...  
                *Prédiction de consommation électrique et émissions de carbone pour des bâtiments municipaux de la ville de Seattle*
                * Fusion / Nettoyage des bases de données
                * Exploration de données
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Imputation et Régression (Linéaire, SVR, Random Forest, Gradient Boosting)
                """),
            "images": ['p_ocr3_1',],
        },
        "p_ocr2": {
            "name": "Nutritionnel",
            "title": (
                f"Nutritional WebApp",
                f"Webapp nutritionnelle"),
            "short": (
                """`Imputation` · `Data Cleaning`, `Classification`  
                Design of an application on nutritional data for public health.""",
                """`Imputation` · `Nettoyage de données`, `Classification`  
                Conception d'une application sur des données nutritionnelles au service de la sante publique."""),
            "description": (
                """
                Ongoing...  
                *Proposal for an application based on nutritional data*
                * Data management / Cleaning
                * Exploring data
                * Concept search
                * Feature engineering (quantitative and qualitative)
                * Imputation (KNN Imputer), Classification (SGD)
                """, """
                En cours...  
                *Proposition d'application basée sur des données nutritionnelles*
                * Gestion / Nettoyage de la base de données
                * Exploration de données
                * Recherche de concepts
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Imputation (KNN Imputer), Classification (SGD)
                """),
            "images": ['p_ocr2_1',],
        },
        "p_m2b": {
            "name": "Neuro-Simulation",
            "title": (
                f"Interface for Neuro-Simulation",
                f"Interface de Simulation Neuronale"),
            "short": (
                """`Modeling` · `Neurosciences`  
                Creation of a simulation, processing and analysis interface for the recognition of activity patterns.""",
                """`Modélisation` · `Neurosciences`  
                Création d'une interface de simulation, traitement et analyse pour la reconnaissance de configurations d'activité."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_m2b_1', 'p_m2b_2', 'p_m2b_3', 'p_m2b_4',],
        },
        "p_m2": {
            "name": "Géophysique",
            "title": (
                f"Géophysics of inclusion",
                f"Géophysique de l'inclusion"),
            "short": (
                """`Modeling` · `Geophysics`  
                Simulation of viscosity during deep rock inclusion.""",
                """`Modélisation` · `Géophysique`  
                Simulation de la viscosité lors d'une inclusion de roche en profondeur."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_m2_1'],
        },
        "p_m1": {
            "name": "Nanofiltration",
            "title": (
                f"Salt Nanofiltration",
                f"Nanofiltration de sels"),
            "short": (
                """`Modeling` · `Nanofiltration`  
                Study of salt nanofiltration by a polyamide-type membrane: Creation of a membrane.""",
                """`Modélisation` · `Nanofiltration`  
                Étude de la nanofiltration de sels par une membrane de type polyamide : Création d'une membrane."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_m1_1', 'p_m1_2'],
        },
        "p_l3": {
            "name": "Ferromagnétisme",
            "title": (
                f"Ferromagnetism - Phase Transition",
                f"Transitions de phase - Ferromagnétisme"),
            "short": (
                """`Modeling` · `Ferromagnetism`  
                Simulation of the Ising Model by ferromagnetic/paramagnetic phase transition.""",
                """`Modélisation` · `Ferromagnétisme`  
                Simulation du Modèle d'Ising par transitions de phase ferromagnétique / paramagnétique."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_l3_1', ],
        },
        "p_iut": {
            "name": "Volcanologie",
            "title": (
                f"Sodium Salt Bevel Elevation Sensor",
                f"Capteur d'élévation du Biseau salé"),
            "short": (
                """`Volcanology` · `Electronics`  
                Development of a measuring instrument specific to the height of a sodium salt bevel: The Biseometer.""",
                """`Volcanologie` · `Électronique`  
                Élaboration d'un instrument de mesures spécifique à la hauteur d'un biseau salé : Le Biseaumètre."""),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "images": ['p_iut_1', ],
        },
    }
    
    header = st.empty()
    d_lines = {}
    tags = [
        list(present_projects),
        list(past_projects),
    ]
    names = [
        [p['name'] for _,p in present_projects.items()],
        [p['name'] for _,p in past_projects.items()],
    ]
    
    # Tabs or Containers
    parts = [
        st.container(),
        st.container(),
    ]
    part_names = [
        'Présents' if sss["lg_key"] else 'Present',
        'Passés' if sss["lg_key"] else 'Past',
    ]
    projects = [
        present_projects,
        past_projects, 
    ]
        
    for ipart, part in enumerate(parts):
        d_lines[ipart] = {}
        part.write(f"<h3 class=\"subheader\">{part_names[ipart]}</h3>", unsafe_allow_html=True)
        containers = [part.container() for _ in names[ipart]]
        
        for container, tag in zip(containers, tags[ipart]):
            if sss['layout'] == 'wide':
                img, title = container.columns((1,4), vertical_alignment='center')
                d_lines[ipart][tag] = img, title, container
            else:
                img, txt = container.columns((1,7))
                d_lines[ipart][tag] = img, txt.empty(), txt
        
    # Content
    header.header(
        "Projets" if sss["lg_key"] else 'Projects', 
        anchor='projects', divider="orange")
    
    for ipart, part in enumerate(parts):
        for tag, c in d_lines[ipart].items():
            project = projects[ipart][tag]
            if sss['layout'] == 'wide':
                c[0].image(sss['images'][tag], width=int(0.3 * sss['layout_width']))
            else:
                c[0].image(sss['images'][tag])
            c[1].write('#### ' + project['title'][sss["lg_key"]])
            with c[2].expander(project['short'][sss["lg_key"]]):
                before = '''
                    <hr style="margin-top:0;">  
                '''
                st.markdown(before + project['description'][sss["lg_key"]], unsafe_allow_html=True)
                for img in project['images']:
                    st.image(sss['images'][img])


if __name__ == "__main__":
    utils.always()
    main()
    utils.background()
