import streamlit as st
from tools import utils
sss = st.session_state


def main():
    xrator = "[XRator](https://www.x-rator.com/)"
    lindera = "[Lindera](https://www.lindera.de/)"
    jl = "[Jagger&Lewis](https://www.jagger-lewis.com/)"
    alpha = "[Alpha Conseil](https://www.alpha-conseils.fr/)"
    oc = "[OpenClassrooms](https://openclassrooms.com/fr/paths/794-machine-learning-engineer#projects)"
    ins = "[INS](https://ins-amu.fr/)"

    jobs = {
        "jl": {
            "name": "Jagger&Lewis",
            "title": (
                f"Data Scientist, {jl}",
                f"Scientifique de la donnée, {jl}"),
            "dateplace": (
                "**1 year** / *2023* / **Lille, France**",
                "**1 an** / *2023* / **Lille**"),
            "short": (
                "Dog behaviour recognition from smart necklace sensors for the well-being of the animal",
                "Reconnaissance du comportement canin à partir de capteurs intelligent de collier pour le bien-être de l'animal"),
            "description": (
                """
                Ongoing...
                * Cleaning, checking and analysing the data
                * Development, maintenance and optimization of algorithms, pipelines and APIs
                """, """
                En cours...
                * Nettoyer, vérifier et analyser les données
                * Développement, maintien et optimisation d'algorithmes, pipelines et APIs
                """),
            "shortskills": (
                "`Python`, `Time Series`, `Kubernetes`, ...",
                "`Python`, `Séries temporelles`, `Kubernetes`, ..."),
            "skills": ("""
                Python · Git · Plotly · Bash · Linux · Windows · Jupyter · Pandas · Scikit-Learn · 
                Docker · Seaborn · Kubernetes · Notion · Shell Scripting · Regular expressions · Web applications · 
                Scaleway · Matplotlib · API REST
                
                Webscrapping · Data Analysis · Signal processing · Machine learning · 
                Natural Language Processing · Numerical Simulation · Classification · 
                Scientific analysis · Algorithmes · Regression modelling · Data cleaning · 
                Time Series · Problem solving · Data Visualization · Data exploration
                
                Agiles methods · R&D · DevOps · Independant
                """, """
                Python · Git · Plotly · Bash · Linux · Windows · Jupyter · Pandas · Scikit-Learn · 
                Docker · Seaborn · Kubernetes · Notion · Shell Scripting · Expressions régulières · Applications web · 
                Scaleway · Matplotlib · API REST
                
                Grattage de données · Analyse de données · Traitement du signal · Apprentissage automatique · 
                Traitement automatique du langage naturel · Simulation Numérique · Classification · 
                Analyses scientifiques · Algorithmes · Modèles de régression · Nettoyage de données · 
                Séries temporelles · Résolution de problèmes · Visualisation de données · Exploration des données
                
                Méthodes agiles · R&D · DevOps · Indépendant
                """),
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
                "Intermediate between Clinical and Data Science",
                "Intermédiaire entre les équipes Clinique et Data Science"),
            "description": (
                """
                Ongoing...
                * Cleaning / Checking / Analysing the data
                * Code Refactoring / Optimization
                """, """
                En cours...
                * Nettoyer, vérifier et analyser les données
                * Refactorisation et optimisation de code
                """),
            "shortskills": (
                "`Python`, `Unstructured data`, `Liaison agent`, ...",
                "`Python`, `Données non structurées`, `Agent de liaison`, ..."),
            "skills": ("""
                Python · Git · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Microsoft Excel
            
                Data Analysis · Adaptation · Unstructured data · Deep Learning · Problem solving · 
                Data Visualization · Research · Data exploration · Data cleaning
                
                Agiles methods · Liaison agent
                """, """
                Python · Git · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Microsoft Excel
            
                Analyse de données · Adaptation · Données non structurées · Deep Learning · Résolution de problèmes · 
                Visualisation de données · Recherche · Exploration des données · Nettoyage de données
                
                Méthodes agiles · Agent de liaison
                """),
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
                "Improving the Cyber Risk Management using data for quantification",
                "Amélioration de la gestion des risques Cyber par l'utilisation des données pour la quantification"),
            "description": (
                """
                Ongoing...
                * Improve Cyber Risk Management and Reporting for IT or CISO
                * Study, Extract, Clean, Manage and Analyze the data
                * Identify gaps and use data for risk quantification
                * Creation/Refactoring/Optimization of code to process the data
                * Studying the state of the art for imputation and classification
                """, """
                En cours...
                * Améliorer la Gestion et le rapport de risque Cyber pour les IT ou RSSI
                * Étudier, Extraire, Nettoyer, Gérer et Analyser les données
                * Création, Refactorisation et Optimisation de code
                * Développement d'outils
                * État de l’art du domaine
                """),
            "shortskills": (
                "`Python`, `Unstructured data`, `NLP`, ...",
                "`Python`, `Données non structurées`, `NLP`, ..."),
            "skills": ("""
                Python · Git · GitLab · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Django · 
                Docker · Seaborn · Kubernetes · OVH · Shell Scripting · Regular expressions · Web applications · 
                API REST · Prefect · NLTK · Spacy · JIRA · AWS · PyTorch · Plotly · Microsoft Azure · MySQL · 
                Scikit-Learn · NoSQL
            
                Webscrapping · Natural Language Processing · Data Analysis · Adaptation · 
                Unstructured data · Imputation · Regression modelling · Classification · Algorithmes · 
                Machine Learning · Deep Learning · Transfert Learning · Problem solving · Partitioning · 
                Data visualization · Research · Data exploration · Data cleaning
                
                Agiles methods · R&D · DevOps · Independant
                """, """
                Python · Git · GitLab · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Django · 
                Docker · Seaborn · Kubernetes · OVH · Shell Scripting · Expressions régulières · Applications web · 
                API REST · Prefect · NLTK · Spacy · JIRA · AWS · PyTorch · Plotly · Microsoft Azure · MySQL · 
                Scikit-Learn · NoSQL
            
                Grattage de données · Traitement automatique du langage naturel · Analyse de données · Adaptation · 
                Données non structurées · Imputation · Modèles de régression · Classification · Algorithmes · 
                Machine Learning · Deep Learning · Transfert Learning · Résolution de problèmes · Partitionnement · 
                Visualisation de données · Recherche · Exploration des données · Nettoyage de données
                
                Méthodes agiles · R&D · DevOps · Indépendant
                """),
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
                "Mentored projects (weekly) including Data Cleaning and Data Analysis",
                "Projets encadrés (hebdomadaire), incluant le nettoyage des données et l'analyse des données"),
            "description": (
                """
                Ongoing...
                * Produce an application for automatic multi-tagging of questions using state of the art algorithms (NLP, XMC, Deep Learning) 
                * Produce an application for race recognition of dog images (Deep Learning, Transfer Learning)
                * Segment customers of an e-commerce website (Unsupervised Learning, KMeans, HCA, DBSCAN)
                * Anticipate a city's electricity consumption and CO² emissions (Supervised Learning, SVM, Random Forest, Boosting, ...)
                * Design of an application on nutritional data for public health
                """, """
                En cours...
                * Produire une application pour l'étiquetage multiple automatique de questions en utilisant les algorithmes les plus récents et performants (SOTA, NLP, XMC, Deep Learning)
                * Produire une application pour la reconnaissance de race d'images de chiens (Deep Learning, Transfer Learning)
                * Segmenter les clients d'un site e-commerce (Apprentissage Non-Supervisé, k-means, HCA, DBSCAN)
                * Anticiper la consommation électrique et les émissions de CO² d'une ville (Apprentissage Supervisé, SVM, Forêt aléatoires, Boosting, ...)
                * Conception d'une application sur des données nutritionnelles au service de la santé publique
                """),
            "shortskills": (
                "`Python`, `Communication`, `State of the art`, ...",
                "`Python`, `Communication`, `État de l\'art`, ..."),
            "skills": ("""
                Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · Django · Kaggle · k-means · Random forest · 
                Boosting · Docker · Seaborn · Shell Scripting · Regular expressions · Web applications · HCA · SVM · 
                API REST · NLTK · AWS · PyTorch · Plotly · MySQL · Scikit-Learn · TensorFlow · XMC · DBSCAN
            
                Webscrapping · Natural Language Processing · Data Analysis · Adaptation · 
                Unstructured data · Imputation · Regression modelling · Classification · Algorithmes · 
                Machine Learning · Deep Learning · Transfert Learning · Problem solving · Partitioning · 
                Data visualization · Research · Data exploration · Data cleaning · Neural Networks · 
                Inverse Problems · Image processing · Communication · Linear algebra · State of the art
                
                Independant
                """, """
                Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · Django · Kaggle · k-means · Forêt aléatoire · 
                Boosting · Docker · Seaborn · Shell Scripting · Expressions régulières · Applications web · HCA · SVM · 
                API REST · NLTK · AWS · PyTorch · Plotly · MySQL · Scikit-Learn · TensorFlow · XMC · DBSCAN
            
                Grattage de données · Traitement automatique du langage naturel · Analyse de données · Adaptation · 
                Données non structurées · Imputation · Modèles de régression · Classification · Algorithmes · 
                Machine Learning · Deep Learning · Transfert Learning · Résolution de problèmes · Partitionnement · 
                Visualisation de données · Recherche · Exploration des données · Nettoyage de données · Neural Networks · 
                Inverse Problems · Traitement de l'image · Communication · Algèbre linéaire · État de l'art
                
                Indépendant
                """),
        },
        "alpha": {
            "name": "Alpha Conseil",
            "title": (
                f"DevOps Engineer, {alpha}",
                f"Ingénieur DevOps, {alpha}"),
            "dateplace": (
                "**7 months** / *2019* / **Paris, France**",
                "**7 mois** / *2019* / **St-Germain-en-Laye**"),
            "short": (
                "Implementing and automation of the coding environment for a web application",
                "Implémentation et automatisation de l'environnement de travail pour une application web"),
            "description": (
                """
                Ongoing...
                """, """
                En cours...
                """),
            "shortskills": (
                "`Python`, `Communication`, `State of the art`, ...",
                "`Python`, `Communication`, `État de l\'art`, ..."),
            "skills": ("""
                Python · Git · Bash · Windows · Linux · Jupyter · Pandas · Django · Microsoft Azure · MySQL · 
                Docker · JIRA · Shell Scripting · Regular expressions · Web applications · API REST · MongoDB
                        
                Front-end · Webscrapping · Algorithmes · Communication
                
                Agiles methods · DevOps
                """, """
                Python · Git · Bash · Windows · Linux · Jupyter · Pandas · Django · Microsoft Azure · MySQL · 
                Docker · JIRA · Shell Scripting · Expressions régulières · Applications web · API REST · MongoDB
                        
                Développement front-end · Grattage de données · Algorithmes · Communication
                
                Méthodes agiles · DevOps
                """),
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
                "Multistability in large scale of brain activity modeling and Funtional Connectivity Dynamics of epilepsy",
                "Multistabilité dans la modélisation de l’activité cérébrale à large échelle et dynamique de la Connectivité Fonctionnelle de l'épilepsie"),
            "description": (
                """
                Ongoing...
                * Comparative analyzes using functional connectivity dynamic between epileptic patients and controls
                * Developing my own simulator, preprocessing/analyzing tools in Python and its scientific libraries
                """, """
                En cours...
                * Analyses comparatives de séries temporelles entre patients épileptiques et contrôles
                * Développement de mon simulateur et outils pour les pré-traitements et analyses
                """),
            "shortskills": (
                "`Python`, `Research`, `State of the art`, ...",
                "`Python`, `Recherche`, `État de l\'art`, ..."),
            "skills": ("""
                Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · k-means · PCA · ICA · 
                Seaborn · Shell Scripting · Regular expressions · Plotly · Scikit-Learn · FCD · HPC
            
                Signal processing · Webscrapping · Data Analysis · Adaptation · Classification · Medical imaging · 
                Algorithmes · Neural networks · Machine Learning · Problem solving · Data visualization · 
                Research · Data exploration · Data cleaning · Communication · Linear algebra · State of the art · 
                Mathematical modelling · Finite element method · Time series
                
                Independant · R&D
                """, """
                Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · k-means · PCA · ICA · 
                Seaborn · Shell Scripting · Expressions régulières · Plotly · Scikit-Learn · FCD · HPC
            
                Traitement du signal · Grattage de données · Analyse de données · Adaptation · Classification · Imagerie Médicale · 
                Algorithmes · Réseaux neuronaux · Machine Learning · Résolution de problèmes · Visualisation de données · 
                Recherche · Exploration des données · Nettoyage de données · Communication · Algèbre linéaire · État de l'art · 
                Modélisation mathématique · Méthode des éléments finis
                
                Indépendant · R&D
                """),
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
                "Study of neuro-dynamic models for the recognition of activity configurations in the resting state (Resting-State Networks)",
                "Etude de modèles neuro-dynamiques pour la reconnaissance de configurations d'activité à l'état de repos (Resting-State Networks)"),
            "description": (
                """
                Ongoing...
                * Creation and study of a dynamic model for publication
                * Machine learning of activity configurations
                * Creation of learning algorithms
                """, """
                En cours...
                * Création et étude d’un modèle dynamique pour publication
                * Apprentissage automatique de configurations d’activité
                * Création d'algorithmes d'apprentissage
                """),
            "shortskills": (
                "`Python`, `Research`, `State of the art`, ...",
                "`Python`, `Recherche`, `État de l\'art`, ..."),
            "skills": ("""
                Python · Git · Matplotlib · Bash · Windows · Jupyter · PCA · ICA · 
                Shell Scripting · Regular expressions · Scikit-Learn · HPC
            
                Signal processing · Data Analysis · Adaptation · Classification · Algorithmes · Neural networks · 
                Problem solving · Data visualization · Research · Data exploration · Data cleaning · 
                Communication · Linear algebra · State of the art · Mathematical modelling · Finite element method · 
                Pattern Recognition · Time series
                
                Independant · R&D
                """, """
                Python · Git · Matplotlib · Bash · Windows · Jupyter · PCA · ICA · 
                Shell Scripting · Expressions régulières · Scikit-Learn · HPC
            
                Traitement du signal · Analyse de données · Adaptation · Classification · Algorithmes · Réseaux neuronaux · 
                Résolution de problèmes · Visualisation de données · Recherche · Exploration des données · Nettoyage de données · 
                Communication · Algèbre linéaire · État de l'art · Modélisation mathématique · Méthode des éléments finis · Pattern Recognition
                
                Indépendant · R&D
                """),
        },
    }

    header = st.empty()
    d_lines = {}
    job_tags = list(jobs)
    job_names = [j['name'] for _,j in jobs.items()]
    
    
    # Tabs or Containers
    if sss['layout'] == "wide":
        containers = st.tabs(job_names)
    else:
        containers = [st.container() for _ in job_names]
    
    for container, job_tag in zip(containers, job_tags):
        if sss['layout'] == 'wide':
            img, title = container.columns((1,4), vertical_alignment='center')
            img.image(sss['images'][job_tag.replace("2", "")])
            d_lines[job_tag] = title, container.empty(), container.empty(), container.empty(), container.empty()
        else:
            img, txt = container.columns((1,5))
            img.image(sss['images'][job_tag.replace("2", "")])
            d_lines[job_tag] = txt.empty(), txt.empty(), txt.empty(), txt.empty(), txt.empty()
            container.write('---')
        
    # Content
    header.header(
        "Expériences" if sss["lg_key"] else 'Experiences', 
        anchor='experiences', divider="orange")
    
    for job_tag, job in jobs.items():
        c = d_lines[job_tag]
        c[0].write('#### ' + job['title'][sss["lg_key"]])
        c[1].markdown(job['dateplace'][sss["lg_key"]])
        c[2].markdown(job['short'][sss["lg_key"]])
        (
            c[3]
            .expander(job['shortskills'][sss["lg_key"]])
            .write(job['skills'][sss["lg_key"]])
        )
        c[4].expander("Description").write(job['description'][sss["lg_key"]])


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
