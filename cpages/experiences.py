import streamlit as st
from tools import utils
sss = st.session_state


def main():
    refrasense = "RefraSense"
    xrator = "[XRator](https://www.x-rator.com/)"
    lindera = "[Lindera](https://www.lindera.de/)"
    jl = "[Jagger&Lewis](https://www.jagger-lewis.com/)"
    alpha = "[Alpha Conseil](https://www.alpha-conseils.fr/)"
    oc = "[OpenClassrooms](https://openclassrooms.com/fr/paths/794-machine-learning-engineer#projects)"
    ins = "[INS](https://ins-amu.fr/)"

    jobs = {
        "refrasense": {
            "name": "RefraSense",
            "title": (
                f"Data Scientist, {refrasense}",
                f"Scientifique de la donnée, {refrasense}"),
            "dateplace": (
                "**2 months** / *2025* / **France**",
                "**2 mois** / *2025* / **France**"),
            "short": (
                """`Freelance` · `Modeling` · `Analysis` · `Regression` · `API`  
                *Develop, optimize and deploy predictive models in the medical sector.*""",
                """`Freelance` · `Modélisation ` · `Analyse` · `Régression` · `API`  
                *Développer, optimiser et déployer des modèles prédictifs dans le médical.*"""),
            "description": (
                """
                **GENERAL**
                * Startup development of an AI-powered solution for automated eyeglass prescriptions.
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Développement d'une solution basée sur l'IA pour les prescriptions automatisées de lunettes.
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Scaleway, Serverless, Windows, Jupyter, Pandas, Scikit-Learn, MLFlow, WandB,
                Docker, Notion, Regular expressions, Web applications, Matplotlib, API REST`
                - Expertise: `Data Analysis, Machine learning, 
                Scientific analysis, Algorithmes, Regression modelling, Data cleaning, 
                Problem solving, Data Visualization, Data exploration`
                - Context: `Freelance, R&D, Independant`""", 
                """
                - Technologies : `Python, Git, Scaleway, Serverless, Windows, Jupyter, Pandas, Scikit-Learn, MLFlow, WandB,
                Docker, Notion, Expressions régulières, Applications web, Matplotlib, API REST`
                - Savoir-faire : `Analyse de données, Apprentissage automatique, 
                Analyses scientifiques, Algorithmes, Modèles de régression, Nettoyage de données, 
                Résolution de problèmes, Visualisation de données, Exploration des données`
                - Contexte : `Freelance, R&D, Indépendant`"""),
        },
        "jl": {
            "name": "Jagger&Lewis",
            "title": (
                f"Data Scientist, {jl}",
                f"Scientifique de la donnée, {jl}"),
            "dateplace": (
                "**1 year** / *2023* / **Lille, France**",
                "**1 an** / *2023* / **Lille**"),
            "short": (
                """`R&D` · `Modeling` · `Analysis` · `BI` · `CI/CD` · `Software Development`  
                *Verification, maintenance and development of pipelines and algorithms for canine behavior recognition from intelligent sensors for the well-being of the animal.*""",
                """`R&D` · `Modélisation ` · `Analyse` · `BI` · `CI/CD` · `Développement Logiciel`  
                *Vérification, maintien et développement des pipelines et algorithmes permettant la reconnaissance du comportement canin à partir de capteurs intelligents pour le bien-être de l'animal.*"""),
            "description": (
                """
                **GENERAL**
                * Study of solutions for storing collected data and tools for analyzing this data
                * Realization of studies illustrating the benefits of algorithms and specific problems associated with dog life
                * Conducting tests on the relevance of solutions
                * Maintaining documentation, tools, and actions
                * Technological watch
                ---
                **MODELING**
                * Definition and implementation of production environment to meet expectations and requirements in terms of availability, service quality, and security
                * Development, maintenance, and optimization of algorithms, pipelines, and APIs
                * Realization of studies illustrating the performance of prediction models
                * Optimization and documentation for access to different pre-treatments and models
                * Cleaning, checking, and analyzing data for validation
                * Switching environment to Serverless and managing Scaleway
                ---
                **ANALYSES & BI**
                * Recognition of unusual animal behaviors according to specific metrics or criteria
                * Creation of an interactive web application for visualizing different types and sources of media and signals
                * Creation of a dashboard from various analytics sources
                * Implementation of the procedure for capturing new data
                * Optimization of the data collection protocol
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Étude de solutions permettant le stockage des données collectées et des outils permettant l'analyse de ces donées
                * Réalisation d'études illustrant le bénéfice des algorithmes et des problématiques particulières associés à la vie du chien
                * Conduite de tests sur la pertinence des solutions
                * Maintien de la documentation, CIR (Crédit d'Impôt Recherche), des outils et actions
                * Veille technologique
                ---
                **MODÉLISATION**
                * Définition et mise en oeuvre de l'environnement technique de production pour répondre aux attentes et éxigences en terme de disponibilité, de qualité de services et de sécurité
                * Développement, maintien et optimisation d'algorithmes, pipelines et APIs
                * Réalisation d'études permettant d'illustrer la performance des modèles de prédiction
                * Optimisation et documentation pour l'accès aux différents pré-traitements et modèles
                * Nettoyage, vérification et analyses des données pour validation
                * Bascule de l'environnement vers du Serverless et gestion de Scaleway
                ---
                **ANALYSES & BI**
                * Reconnaissance de comportements inhabituels de l'animal selon des métriques ou critères particuliers
                * Création d'une application web intéractive pour la visualisation des différentes types et sources de média et signaux
                * Création d'un tableau de bord à partir de différentes sources d'analytics
                * Mise en oeuvre de la procédure de capture de nouvelles données
                * Optimisation du protocole de collecte des données
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Plotly, Bash, Linux, Windows, Jupyter, Pandas, Scikit-Learn, 
                Docker, Seaborn, Kubernetes, Notion, Shell Scripting, Regular expressions, Web applications, 
                Scaleway, Matplotlib, API REST`
                - Expertise: `Webscrapping, Data Analysis, Signal processing, Machine learning, 
                Natural Language Processing, Numerical Simulation, Classification, 
                Scientific analysis, Algorithmes, Regression modelling, Data cleaning, 
                Time Series, Problem solving, Data Visualization, Data exploration`
                - Context: `Agiles methods, R&D, DevOps, Independant`""", 
                """
                - Technologies : `Python, Git, Plotly, Bash, Linux, Windows, Jupyter, Pandas, Scikit-Learn, 
                Docker, Seaborn, Kubernetes, Notion, Shell Scripting, Expressions régulières, Applications web, 
                Scaleway, Matplotlib, API REST`
                - Savoir-faire : `Grattage de données, Analyse de données, Traitement du signal, Apprentissage automatique, 
                Traitement automatique du langage naturel, Simulation Numérique, Classification, 
                Analyses scientifiques, Algorithmes, Modèles de régression, Nettoyage de données, 
                Séries temporelles, Résolution de problèmes, Visualisation de données, Exploration des données`
                - Contexte : `Méthodes agiles, R&D, DevOps, Indépendant`"""),
        },
        "lindera": {
            "name": "Lindera",
            "title": (
                f"Data Scientist Clinical, {lindera}",
                f"Scientifique de la donnée Clinique, {lindera}"),
            "dateplace": (
                "**2 months** / *2023* / **Italy and Germany**",
                "**2 mois** / *2023* / **Italie et Allemagne**"),
            "short": (
                """`R&D` · `Healthcare` · `Analysis`  
                *Intermediate between Clinical and Data Science teams for the development of a medical device to predict falls in elderly people.*""",
                """`R&D` · `Médical` · `Analyse`  
                *Intermédiaire entre les équipes Clinique et Data Science pour le développement d'un dispositif médical de prédiction de chute des personnes agées.*"""),
            "description": (
                """
                **GENERAL**
                * Cleaning / Checking / Analysing the data
                * Code Refactoring / Optimization
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Nettoyer, vérifier et analyser les données
                * Refactorisation et optimisation de code
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Matplotlib, Bash, Linux, Windows, Jupyter, Pandas, Microsoft Excel`
                - Expertise: `Data Analysis, Adaptation, Unstructured data, Deep Learning, Problem solving, 
                Data Visualization, Research, Data exploration, Data cleaning`
                - Context: `Agiles methods, Liaison agent`""", 
                """
                - Technologies : `Python, Git, Matplotlib, Bash, Linux, Windows, Jupyter, Pandas, Microsoft Excel`
                - Savoir-faire : `Analyse de données, Adaptation, Données non structurées, Deep Learning, Résolution de problèmes, 
                Visualisation de données, Recherche, Exploration des données, Nettoyage de données`
                - Contexte : `Méthodes agiles, Agent de liaison`"""),
        },
        "xrator": {
            "name": "XRator",
            "title": (
                f"Data Scientist, {xrator}",
                f"Scientifique de la donnée, {xrator}"),
            "dateplace": (
                "**9 months** / *2022* / **France and Vietnam**",
                "**9 mois** / *2022* / **France et Vietnam**"),
            "short": (
                """`R&D` · `Cybersecurity` · `Analysis` · `Software Development`  
                *Improve Cyber Risk Management for IT or RSSI by analyzing and managing data, developing information extraction tools.*""",
                """`R&D` · `Cybersecurité` · `Analyse` · `Développement Logiciel`  
                *Améliorer la gestion des risques cyber pour les IT ou RSSI en analysant et gérant les données, en développant des outils d'extraction de l'information.*"""),
            "description": (
                """
                **GENERAL**
                * Improve Cyber Risk Management and Reporting for IT or CISO
                * Study, Extract, Clean, Manage and Analyze the data
                * Identify gaps and use data for risk quantification
                * Creation/Refactoring/Optimization of code to process the data
                * Studying the state of the art for imputation and classification
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Améliorer la Gestion et le rapport de risque Cyber pour les IT ou RSSI
                * Étudier, Extraire, Nettoyer, Gérer et Analyser les données
                * Création, Refactorisation et Optimisation de code
                * Développement d'outils
                * État de l’art du domaine
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, GitLab, Matplotlib, Bash, Linux, Windows, Jupyter, Pandas, Django, 
                Docker, Seaborn, Kubernetes, OVH, Shell Scripting, Regular expressions, Web applications, 
                API REST, Prefect, NLTK, Spacy, JIRA, AWS, PyTorch, Plotly, Microsoft Azure, MySQL, 
                Scikit-Learn, NoSQL`
                - Expertise: `Webscrapping, Natural Language Processing, Data Analysis, Adaptation, 
                Unstructured data, Imputation, Regression modelling, Classification, Algorithmes, 
                Machine Learning, Deep Learning, Transfert Learning, Problem solving, Partitioning, 
                Data visualization, Research, Data exploration, Data cleaning`
                - Context: `Agiles methods, R&D, DevOps, Independant`""", 
                """
                - Technologies : `Python, Git, GitLab, Matplotlib, Bash, Linux, Windows, Jupyter, Pandas, Django, 
                Docker, Seaborn, Kubernetes, OVH, Shell Scripting, Expressions régulières, Applications web, 
                API REST, Prefect, NLTK, Spacy, JIRA, AWS, PyTorch, Plotly, Microsoft Azure, MySQL, 
                Scikit-Learn, NoSQL`
                - Savoir-faire : `Grattage de données, Traitement automatique du langage naturel, Analyse de données, Adaptation, 
                Données non structurées, Imputation, Modèles de régression, Classification, Algorithmes, 
                Machine Learning, Deep Learning, Transfert Learning, Résolution de problèmes, Partitionnement, 
                Visualisation de données, Recherche, Exploration des données, Nettoyage de données`
                - Contexte : `Méthodes agiles, R&D, DevOps, Indépendant`"""),
        },
        "oc": {
            "name": "OpenClassrooms",
            "title": (
                f"Machine Learning Engineer (Internship), {oc}",
                f"Stage Ingénieur Machine Learning, {oc}"),
            "dateplace": (
                "**8 month** / *2021* / **Lille, France**",
                "**8 mois** / *2021* / **Lille**"),
            "short": (
                """`Modeling` · `Healthcare` · `Energy` · `E-commerce` · `Computer Vision` · `Finance` · `Software Development`  
                *A variety of concrete cases of companies managed independently with a weekly mentoring and systematically submitted reports, versioned code and presentations to a jury for validation.*""",
                """`Modélisation` · `Santé` · `Énergie` · `E-commerce` · `Analyse d'Image` · `Finances` · `Développement Logiciel`  
                *Différents cas concrets d’entreprise gérés indépendamment avec un mentorat hebdomadaire et soumis systématiquement par des rapports, codes versionnés et présentations en face d’un jury pour validation.*"""),
            "description": (
                """
                **PARTICIPATING IN A KAGGLE COMPETITION**  
                *Predicting cryptocurrency markets based on data collected by G-Research*
                * State-of-the-art study
                * Signal processing
                * Feature engineering (delays, aggregations)
                * Regression (Linear, Light Gradient Boosting Machine, XGBoost)
                * Hyperparameter optimization
                * Using and contributing to other kernels
                ---
                **AUTOMATICALLY CATEGORIZING QUESTIONS**  
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
                ---
                **CLASSIFYING IMAGES USING DEEP LEARNING ALGORITHMS**  
                *Using Deep Learning models for an animal association wanting to automate breed identification*
                * Image processing
                * Supervised classification with multiple classes
                * Creating or implementing existing neural networks
                * Transfer learning (MobileNetV2)
                * Hyperparameter optimization
                * Creating an API in the form of an online application (Streamlit)
                ---
                **SEGMENTING ONLINE SHOP CUSTOMERS**  
                *Providing marketing teams with a segmentable client segmentation to optimize communication campaigns*
                * Merging / Cleaning multiple databases
                * Exploring data
                * Feature engineering (quantitative and qualitative)
                * Unsupervised classification (k-Means, Hierarchical Agglomerative Clustering, DBSCAN)
                * Hyperparameter optimization
                ---
                **ANTICIPATING ELECTRICITY CONSUMPTION NEEDS IN BUILDINGS**  
                *Predicting electricity consumption and carbon emissions for municipal buildings in Seattle*
                * Merging / Cleaning databases
                * Exploring data
                * Feature engineering (quantitative and qualitative)
                * Imputation and Regression (Linear, SVR, Random Forest, Gradient Boosting)
                ---
                **DEVELOPING AN APPLICATION FOR PUBLIC HEALTH**  
                *Proposal for an application based on nutritional data*
                * Data management / Cleaning
                * Exploring data
                * Concept search
                * Feature engineering (quantitative and qualitative)
                * Imputation (KNN Imputer), Classification (SGD)
                ---
                **COMPETENCIES**
                """, """
                **PARTICIPER À UNE COMPETITION KAGGLE**  
                *Prédiction du marché des crypto-monnaies à partir des données amassées par G-Research*
                * État de l’art
                * Traitement du signal
                * Ingénierie des caractéristiques (latences, agrégations)
                * Régression (Linéaire, Light Gradient Boosting Machine, XGBoost)
                * Optimisation des hyperparamètres
                * Utilisation et contribution aux autres kernels
                ---
                **CATÉGORISER AUTOMATIQUEMENT DES QUESTIONS**  
                *Développer un système permettant de tagger automatiquement les questions des utilisateurs sur le site Stack Overflow*
                * Nettoyage (NLTK) et exploration des données
                * Ingénierie des caractéristiques (quantitatives et qualitatives) 
                * Classification multi-étiquette extrême XMC (Gaussian Naive Bayes, Decision Tree Classifier, Linear Support Vector Classification, Multilabel k-Nearest Neighbours)
                * Méthodes (Word Embedding, Binary Relevance, Label Powerset, Classifier Chain)
                * Optimisation des hyperparamètres
                * Création d’un modèle personnel
                * Étude bibliographique de l’état de l’art
                * Implémentation de modèles plus récents (XR-Linear, XR-Transformer)
                * Création d’API sous forme d’une application en ligne (Streamlit)
                ---
                **CLASSER DES IMAGES À L'AIDE D'ALGORITHMES DE DEEP LEARNING**  
                *Utilisation de modèles de Deep Learning pour une association animalière souhaitant automatiser l'identification de races*
                * Traitement d’images
                * Classification supervisée à classes multiples
                * Création ou implémentation de Réseaux Neuronaux existants
                * Apprentissage par transfert (MobileNetV2)
                * Optimisation des hyperparamètres
                * Création d’API sous forme d’une application en ligne (Streamlit)
                ---
                **SEGMENTER DES CLIENTS D'UN SITE E-COMMERCE**  
                *Fournir aux équipes marketing une segmentation activable de leurs clients pour optimiser les campagnes de communication*
                * Fusion / Nettoyage de multiples bases de données
                * Exploration de données
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Classification non supervisée (k-Means, Hiérarchique agglomératif, DBSCAN)
                * Optimisation des hyperparamètres
                ---
                **ANTICIPER LES BESOINS EN CONSOMMATION ÉLECTRIQUE DE BÂTIMENTS**  
                *Prédiction de consommation électrique et émissions de carbone pour des bâtiments municipaux de la ville de Seattle*
                * Fusion / Nettoyage des bases de données
                * Exploration de données
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Imputation et Régression (Linéaire, SVR, Random Forest, Gradient Boosting)
                ---
                **CONCEPTION D’UNE APPLICATION AU SERVICE DE LA SANTE PUBLIQUE**  
                *Proposition d’application basée sur des données nutritionnelles*
                * Gestion / Nettoyage de la base de données
                * Exploration de données
                * Recherche de concepts
                * Ingénierie des caractéristiques (quantitatives et qualitatives)
                * Imputation (KNN Imputer), Classification (SGD)
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Matplotlib, Bash, Windows, Jupyter, Pandas, Django, Kaggle, k-means, Random forest, 
                Boosting, Docker, Seaborn, Shell Scripting, Regular expressions, Web applications, HCA, SVM, 
                API REST, NLTK, AWS, PyTorch, Plotly, MySQL, Scikit-Learn, TensorFlow, XMC, DBSCAN`
                - Expertise: `Webscrapping, Natural Language Processing, Data Analysis, Adaptation, 
                Unstructured data, Imputation, Regression modelling, Classification, Algorithmes, 
                Machine Learning, Deep Learning, Transfert Learning, Problem solving, Partitioning, 
                Data visualization, Research, Data exploration, Data cleaning, Neural Networks, 
                Inverse Problems, Image processing, Communication, Linear algebra, State of the art`
                - Context: `Independant`""", 
                """
                - Technologies : `Python, Git, Matplotlib, Bash, Windows, Jupyter, Pandas, Django, Kaggle, k-means, Forêt aléatoire, 
                Boosting, Docker, Seaborn, Shell Scripting, Expressions régulières, Applications web, HCA, SVM, 
                API REST, NLTK, AWS, PyTorch, Plotly, MySQL, Scikit-Learn, TensorFlow, XMC, DBSCAN`
                - Savoir-faire : `Grattage de données, Traitement automatique du langage naturel, Analyse de données, Adaptation, 
                Données non structurées, Imputation, Modèles de régression, Classification, Algorithmes, 
                Machine Learning, Deep Learning, Transfert Learning, Résolution de problèmes, Partitionnement, 
                Visualisation de données, Recherche, Exploration des données, Nettoyage de données, Neural Networks, 
                Inverse Problems, Traitement de l'image, Communication, Algèbre linéaire, État de l'art`
                - Contexte : `Indépendant`"""),
        },
        "alpha": {
            "name": "Alpha Conseil",
            "title": (
                f"DevOps Engineer, {alpha}",
                f"Ingénieur DevOps, {alpha}"),
            "dateplace": (
                "**7 months** / *2019* / **Paris, France**",
                "**7 mois** / *2019* / **Paris**"),
            "short": (
                """`Accounting Expertise` · `CI/CD` · `Web Design` · `Software Development`  
                *Implementation and automation of an environment for a web-based platform to connect professionals with chartered accountants.*""",
                """`Expertise Comptable` · `CI/CD` · `Conception Web` · `Développement Logiciel`  
                *Implémentation et automatisation de l'environnement pour une interface web de mise en relation entre professionnels et experts comptables.*"""),
            "description": (
                """
                **WORKING IN AGILE SCRUM METHODOLOGY**
                * Sprint Planning Organisation and ticket allocation from Backlog,
                * Daily meeting for progress, blockers, updates, and Kanban tracking
                * Grooming (Story Review) meeting to analyze tickets, prepare upcoming sprints
                * Poker planning to estimate ticket values
                * Sprint Review meeting to analyze completed sprint
                * Demo and Retrospective
                --- 
                **COLLABORATIVE TASKS WITH TEAMS**
                * Participation in technology choices, adoption of frameworks and tools
                * Development of applications for evolution and correction
                * Creation, modification of pages and forms based on User Stories (US)
                * Integration of Bootstrap (responsive design), slides, and pop-ups in JavaScript
                * Mastery of the MVC architecture (Models-View-Templates for Django)
                * Migration of Pipelines to Controllers
                * Control of versioning, deployment, and review of technical documentation and code
                --- 
                **INDIVIDUAL PROJECTS AND TASKS**
                * Creation of a development environment adaptable to all system environments
                * Creation, development of code under VS Code in Python / Django / HTML5 / CSS3
                * Optimization of different parts and types of code
                * Writing technical documentation for the code and development environment (Markdown) and automating documentation
                * Training teams on various tools (Django/Jupyter)
                * Conducting unit tests
                --- 
                **COMPETENCIES**
                """, """
                **TRAVAIL EN MÉTHODE AGILE SCRUM**
                * Sprint Planning Organisation et répartition des tickets du Backlog,
                * Daily meeting point d’avancement, point bloquant, màj et suivi du Kanban
                * Grooming (Story Review) réunion d’analyse des tickets, Préparation des sprints à venir
                * Poker planning chiffrage des tickets
                * Sprint Review réunion d’analyse du Sprint écoulé
                * Démo et Rétro
                ---
                **TAVAUX EN COMMUN DES ÉQUIPES**
                * Participation au choix technologique, Appropriation des Framework et outils
                * Développement d’application d’évolutions et de correctifs
                * Création, Modification de pages et de formulaires en fonction des US
                * Intégration de Bootstrap (responsive design), de slides et des Pop-ups en javascript
                * Maitrise de l’architecture MVC (Modèles-Vue-Template pour Django)
                * Migration de Pipelines en Contrôleurs
                * Contrôle du versioning, du déploiement et revu de documentations techniques et de code
                ---
                **PROJETS ET TRAVAUX INDIVIDUEL**
                * Création de l’environnement de développement adapté pour tout environnement système
                * Création, développement du code sous VS Code en Python / Django / HTML5 / CSS3
                * Optimisation des différentes parties et types de code
                * Rédaction de documentations techniques du code et de l’environnement de développement (Markdown) et automatisation de la documentation
                * Formation des équipes aux différents outils (Django/Jupyter)
                * Réalisation de test unitaires
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Bash, Windows, Linux, Jupyter, Pandas, Django, Microsoft Azure, MySQL, 
                Docker, JIRA, Shell Scripting, Regular expressions, Web applications, API REST, MongoDB, 
                JavaScript, JQuery, Ajax, HTML5, CSS3, Bitbucket, Trello, Jira, Slack, VS Code`
                - Expertise: `Front-end development, Webscrapping, Algorithmes, Communication`
                - Context: `Agiles methods, DevOps`""", 
                """
                - Technologies : `Python, Git, Bash, Windows, Linux, Jupyter, Pandas, Django, Microsoft Azure, MySQL, 
                Docker, JIRA, Shell Scripting, Expressions régulières, Applications web, API REST, MongoDB, 
                JavaScript, JQuery, Ajax, HTML5, CSS3, Bitbucket, Trello, Jira, Slack, VS Code`
                - Savoir-faire : `Développement front-end, Grattage de données, Algorithmes, Communication`
                - Contexte : `Méthodes agiles, DevOps`"""),
        },
        "ins": {
            "name": "INS",
            "title": (
                f"PhD Candidate in Computational Neurosciences, {ins}",
                f"Doctorant en Neurosciences Computationnelles, {ins}"),
            "dateplace": (
                "**4 years** / *2013* / **Marseille, France**",
                "**4 ans** / *2013* / **Marseille**"),
            "short": (
                """`Research` · `Neurosciences` · `Modeling` · `Simulation` · `Epilepsy` · `Time Series`  
                *Experience in computational biology for neuroscience, with deep learning projects, neural model creation and signal processing.
                Involved in various literature reviews, data treatment tools creations and visualizations.*
                """, 
                """`Recherche` · `Neurosciences` · `Modélisation` · `Simulation` · `Epilepsie` · `Séries Temporelles`  
                *Expérience dans le domaine de la biologie computationnelle en neurosciences, avec des projets d'apprentissage approfondi, création de modèles neuronaux et traitement du signal.
                Impliqué dans diverses études bibliographiques, créations d'outils de traitements de données et visualisations.*"""),
            "description": (
                """
                **GENERAL**
                * Bibliographic study of the state-of-the-art in the field
                * Study and presentation to the group of external scientific publications not from the laboratory
                * Creation of data treatment tools and visualizations
                * Management of simulation data distributed over multiple parameters
                * Automatic launch procedure for simulations and processing on a calculation cluster
                * Administration of certain aspects of the calculation cluster
                ---
                **DEEP LEARNING PROJECT**
                * Use of simple models (dynamics) to extract activity configurations (schemes) from anatomical structural connectivity (network)
                * Confrontation of extracted configurations with observed configurations in healthy human subjects
                * Automated learning of configurations
                * Modification and optimization of learning algorithms
                ---
                **NEURAL MODEL PROJECT**
                * Systematic creation and analysis of a new model of neuronal population, multi-stable at large scale
                * Creation of a simulation software (optimized for intense calculations)
                * Computationally intensive research to test the model on all its parameters
                * Confrontation of the model's parameters with biological theories of brain functioning
                ---
                **SIGNAL PROCESSING PROJECT**
                * Comparative analyses by dynamic functional connectivity between epileptic patients and controls
                * Parallelization for intense calculations on multiple dimensions
                * Post-processing of time series
                * Analysis of dynamic networks
                * Unsupervised automated learning
                * Research on artifacts and statistical studies
                * Study and critique of a new analytical tool
                * Creation and study of another more advanced tool
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Étude bibliographique de l’état de l’art du domaine
                * Étude de publications scientifiques externes au laboratoire et présentation au groupe
                * Création d’outils de traitements de données et de visualisations
                * Gestion des données de simulations réparties sur de multiples paramètres
                * Procédure de lancement automatique de simulation et de traitement sur cluster de calcul
                * Administration de certains aspects du cluster de calculs
                ---
                **PROJET D'APPRENTISSAGE APPROFONDI**
                * Utilisation de modèles simples (dynamique) pour extraire les configurations d’activité (schémas) à partir d’une connectivité structurelle anatomique (réseau)
                * Confrontation des configurations extraites avec des configurations observées chez des sujets humains sains
                * Apprentissage automatique de configurations
                * Modification et optimisation d’algorithmes d’apprentissage
                ---
                **PROJET MODÈLE NEURONAL**
                * Création et analyse systémique d’un nouveau modèle de population de neurones, multi-stable à large échelle
                * Création d’un logiciel de simulation (optimisation pour des calculs intensifs)
                * Recherche computationnelle intensive pour tester le modèle sur tous ses paramètres
                * Confrontation des paramètres du modèle avec les théories biologiques du fonctionnement cérébral
                ---
                **PROJET TRAITEMENT DU SIGNAL**
                * Analyses comparatives par connectivité fonctionnelle dynamique entre patients épileptiques et contrôles
                * Parallélisation pour les calculs intensifs sur les multiples dimensions
                * Post-traitement des séries temporelles
                * Analyse des réseaux dynamiques
                * Apprentissage automatique non supervisé
                * Recherche d’artefacts et études statistiques
                * Étude et critique d’un nouvel outil d’analyse
                * Création et étude d’un autre outil plus poussé
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, MATLAB, Git, Matplotlib, Bash, Jupyter, Pandas, k-means, PCA, ICA, LateX, 
                Seaborn, Shell Scripting, Regular expression, Plotly, Scikit-Learn, FCD, HPC, Linux, Windows`
                - Expertise: `Signal processing, Webscrapping, Data Analysis, Adaptation, Classification, Medical imaging, 
                Algorithms, Neural networks, Machine Learning, Problem solving, Data visualization, 
                Research, Data exploration, Data cleaning, Communication, Linear algebra, State of the art, 
                Mathematical modelling, Finite element method, Time series`
                - Context: `Independant, R&D`""", 
                """
                - Technologies : `Python, MATLAB, Git, Matplotlib, Bash, Jupyter, Pandas, k-means, PCA, ICA, LateX, 
                Seaborn, Shell Scripting, Expressions régulières, Plotly, Scikit-Learn, FCD, HPC, Linux, Windows`
                - Savoir-faire : `Traitement du signal, Grattage de données, Analyse de données, Adaptation, Classification, Imagerie Médicale, 
                Algorithmes, Réseaux neuronaux, Machine Learning, Résolution de problèmes, Visualisation de données, 
                Recherche, Exploration des données, Nettoyage de données, Communication, Algèbre linéaire, État de l'art, 
                Modélisation mathématique, Méthode des éléments finis`
                - Contexte : `Indépendant, R&D`"""),
        },
        "ins2": {
            "name": "INS",
            "title": (
                f"Assistant Engineer, {ins}",
                f"Assistant Ingénieur, {ins}"),
            "dateplace": (
                "**9 months** / *2013* / **Marseille, France**",
                "**9 mois** / *2013* / **Marseille**"),
            "short": (
                """`Research` · `Neurosciences` · `Modeling` · `Simulation`  
                *Study of neuro-dynamic models for the recognition of activity configurations in the resting state (Resting-State Networks).*""",
                """`Recherche` · `Neurosciences` · `Modélisation` · `Simulation`  
                *Etude de modèles neuro-dynamiques pour la reconnaissance de configurations d'activité à l'état de repos (Resting-State Networks).*"""),
            "description": (
                """
                **GENERAL**
                * Bibliographic study of the state-of-the-art in the field
                * Study and presentation to the group of external scientific publications not from the laboratory
                * Creation of data treatment tools and visualizations
                ---
                **NEURAL MODEL PROJECT**
                * Systematic creation and analysis of a new model of neuronal population, multi-stable at large scale
                * Creation of a simulation software (optimized for intense calculations)
                * Confrontation of the model's parameters with biological theories of brain functioning
                ---
                **COMPETENCIES**
                """, """
                **GÉNÉRAL**
                * Étude bibliographique de l’état de l’art du domaine
                * Étude de publications scientifiques externes au laboratoire et présentation au groupe
                * Création d’outils de traitements de données et de visualisations
                ---
                **PROJET MODÈLE NEURONAL**
                * Création et analyse systémique d’un nouveau modèle de population de neurones, multi-stable à large échelle
                * Création d’un logiciel de simulation (optimisation pour des calculs intensifs)
                * Confrontation des paramètres du modèle avec les théories biologiques du fonctionnement cérébral
                ---
                **COMPÉTENCES**
                """),
            "skills": (
                """
                - Technologies: `Python, Git, Matplotlib, Bash, Jupyter, PCA, ICA, LateX, 
                Shell Scripting, Regular expression, Scikit-Learn, HPC, Windows, Linux`
                - Expertise: `Signal processing, Data Analysis, Adaptation, Classification, 
                Algorithms, Neural networks, Problem solving, Data visualization, 
                Research, Data exploration, Communication, Linear algebra, State of the art, 
                Mathematical modelling, Finite element method, Pattern Recognition, Time series`
                - Context: `Independant, R&D`""", 
                """
                - Technologies : `Python, Git, Matplotlib, Bash, Jupyter, PCA, ICA, LateX, 
                Shell Scripting, Expressions régulières, Scikit-Learn, HPC, Windows, Linux`
                - Savoir-faire : `Traitement du signal, Analyse de données, Adaptation, Classification, 
                Algorithmes, Réseaux neuronaux, Résolution de problèmes, Visualisation de données, 
                Recherche, Exploration des données, Communication, Algèbre linéaire, État de l'art, 
                Modélisation mathématique, Pattern Recognition, Méthode des éléments finis`
                - Contexte : `Indépendant, R&D`"""),
        },
    }

    header = st.empty()
    d_lines = {}
    job_tags = list(jobs)
    job_names = [j['name'] for _,j in jobs.items()]
    
    
    # Tabs or Containers
    if sss['layout'] == "wide":
        # containers = st.tabs(job_names)
        containers = [st.container() for _ in job_names]
    else:
        containers = [st.container() for _ in job_names]
    
    for container, job_tag in zip(containers, job_tags):
        if sss['layout'] == 'wide':
            img, title = container.columns((1,4), vertical_alignment='center')
            img.image(sss['images'][job_tag.replace("2", "")])
            d_lines[job_tag] = title, container.empty(), container.empty()
        else:
            img, txt = container.columns((1,7))
            img.image(sss['images'][job_tag.replace("2", "")])
            d_lines[job_tag] = txt.empty(), txt.empty(), txt.empty()
        
    # Content
    header.header(
        "Expériences" if sss["lg_key"] else 'Experiences', 
        anchor='experiences', divider="orange")
    
    for job_tag, job in jobs.items():
        c = d_lines[job_tag]
        c[0].write('#### ' + job['title'][sss["lg_key"]])
        c[1].markdown(job['dateplace'][sss["lg_key"]])
        with c[2].expander(job['short'][sss["lg_key"]]):
            before = '''
                <hr style="margin-top:0;">  
            '''
            st.markdown(before + job['description'][sss["lg_key"]], unsafe_allow_html=True)
            st.write(job['skills'][sss["lg_key"]].replace(', \n', '` · `').replace(', ', '` · `'))
        # with c[2].popover(job['short'][sss["lg_key"]] + '\n\n...', use_container_width=True):
        #     st.write(job['description'][sss["lg_key"]])
        #     st.write(job['skills'][sss["lg_key"]].replace(', \n', '` · `').replace(', ', '` · `'))


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
