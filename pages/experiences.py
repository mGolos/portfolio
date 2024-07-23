import utils
import streamlit as st
sss = st.session_state


def main():
    xrator = "[XRator](https://www.x-rator.com/)"
    lindera = "[Lindera](https://www.lindera.de/)"
    jl = "[Jagger&Lewis](https://www.jagger-lewis.com/)"
    alpha = "[Alpha Conseil](https://www.alpha-conseils.fr/)"
    oc = "[OpenClassrooms](https://openclassrooms.com/fr/paths/794-machine-learning-engineer#projects)"
    ins = "[INS](https://ins-amu.fr/)"

    header = st.empty()
    d_lines = {}
    job_tags = ['jl', 'lindera', 'xrator', 'oc', 'alpha', 'ins', 'ins2']
    job_names = ['Jagger&Lewis', 'Lindera', 'XRator', 'OpenClassrooms', 'Alpha Conseil', 'INS', 'INS']
    
    
    # Tabs or Containers
    if sss['layout'] == "wide":
        containers = st.tabs(job_names)
    else:
        containers = [st.container() for _ in job_names]
    
    for container, job_name in zip(containers, job_tags):
        img, txt = container.columns((1,5))
        container.write('---')
        img.image(sss['images'][job_name.replace("2", "")])
        d_lines[job_name] = txt.empty(), txt.empty(), txt.empty()
    
    
    if sss['language'] == "fr":
        header.header("Expériences", anchor='experiences', divider="orange")
        
        d_lines['jl'][0].write(f"#### Scientifique de la donnée, {jl}")
        d_lines['jl'][1].markdown("""
            **1 an** / *2023* / **Lille**
            * Reconnaissance de comportement de l'animal
            * Nettoyer, vérifier et analyser les données
            * Développement, maintien et optimisation d'algorithmes, pipelines et APIs
        """)
        d_lines['jl'][2].expander('`Python`, `Séries temporelles`, `Kubernetes`, ...').write("""
            Python · Git · Plotly · Bash · Linux · Windows · Jupyter · Pandas · Scikit-Learn · 
            Docker · Seaborn · Kubernetes · Notion · Shell Scripting · Expressions régulières · Applications web · 
            Scaleway · Matplotlib · API REST
            
            Grattage de données · Analyse de données · Traitement du signal · Apprentissage automatique · 
            Traitement automatique du langage naturel · Simulation Numérique · Classification · 
            Analyses scientifiques · Algorithmes · Modèles de régression · Nettoyage de données · 
            Séries temporelles · Résolution de problèmes · Visualisation de données · Exploration des données
            
            Méthodes agiles · R&D · DevOps · Indépendant
        """)
        
        d_lines['lindera'][0].write(f"#### Scientifique de la donnée Clinique, {lindera}")
        d_lines['lindera'][1].markdown("""
            **2 mois** / *2023* / **Italie et Allemagne**
            * Intermédiaire entre les équipes Clinique et Data Science
            * Nettoyer, vérifier et analyser les données
            * Refactorisation et optimisation de code
        """)
        d_lines['lindera'][2].expander('`Python`, `Données non structurées`, `Agent de liaison`, ...').write("""
            Python · Git · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Microsoft Excel
           
            Analyse de données · Adaptation · Données non structurées · Deep Learning · Résolution de problèmes · 
            Visualisation de données · Recherche · Exploration des données · Nettoyage de données
            
            Méthodes agiles · Agent de liaison
        """)
        
        d_lines['xrator'][0].write(f"#### Scientifique de la donnée, {xrator}")
        d_lines['xrator'][1].markdown("""
            **9 mois** / *2022* / **France et Vietnam**
            * Améliorer la Gestion et le rapport de risque Cyber pour les IT ou RSSI
            * Étudier, Extraire, Nettoyer, Gérer et Analyser les données
            * Création, Refactorisation et Optimisation de code
            * Développement d'outils
            * État de l’art du domaine
        """)
        d_lines['xrator'][2].expander('`Python`, `Données non structurées`, `NLP`, ...').write("""
            Python · Git · GitLab · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Django · 
            Docker · Seaborn · Kubernetes · OVH · Shell Scripting · Expressions régulières · Applications web · 
            API REST · Prefect · NLTK · Spacy · JIRA · AWS · PyTorch · Plotly · Microsoft Azure · MySQL · 
            Scikit-Learn · NoSQL
           
            Grattage de données · Traitement automatique du langage naturel · Analyse de données · Adaptation · 
            Données non structurées · Imputation · Modèles de régression · Classification · Algorithmes · 
            Machine Learning · Deep Learning · Transfert Learning · Résolution de problèmes · Partitionnement · 
            Visualisation de données · Recherche · Exploration des données · Nettoyage de données
            
            Méthodes agiles · R&D · DevOps · Indépendant
        """)
        
        d_lines['oc'][0].write(f"#### Stage Ingénieur Machine Learning, {oc}")
        d_lines['oc'][1].markdown("""
            **8 mois** / *2021* / **Lille**  
            Projets encadrés (hebdomadaire), incluant le nettoyage des données et l'analyse des données :
            * Produire une application pour l'étiquetage multiple automatique de questions en utilisant les algorithmes les plus récents et performants (SOTA, NLP, XMC, Deep Learning)
            * Produire une application pour la reconnaissance de race d'images de chiens (Deep Learning, Transfer Learning)
            * Segmenter les clients d'un site e-commerce (Apprentissage Non-Supervisé, k-means, HCA, DBSCAN)
            * Anticiper la consommation électrique et les émissions de CO² d'une ville (Apprentissage Supervisé, SVM, Forêt aléatoires, Boosting, ...)
            * Conception d'une application sur des données nutritionnelles au service de la santé publique
        """)
        d_lines['oc'][2].expander('`Python`, `Communication`, `État de l\'art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · Django · Kaggle · k-means · Forêt aléatoire · 
            Boosting · Docker · Seaborn · Shell Scripting · Expressions régulières · Applications web · HCA · SVM · 
            API REST · NLTK · AWS · PyTorch · Plotly · MySQL · Scikit-Learn · TensorFlow · XMC · DBSCAN
           
            Grattage de données · Traitement automatique du langage naturel · Analyse de données · Adaptation · 
            Données non structurées · Imputation · Modèles de régression · Classification · Algorithmes · 
            Machine Learning · Deep Learning · Transfert Learning · Résolution de problèmes · Partitionnement · 
            Visualisation de données · Recherche · Exploration des données · Nettoyage de données · Neural Networks · 
            Inverse Problems · Traitement de l'image · Communication · Algèbre linéaire · État de l'art
            
            Indépendant
        """)
        
        d_lines['alpha'][0].write(f"#### Ingénieur DevOps, {alpha}")
        d_lines['alpha'][1].markdown("""
            **7 mois** / *2019* / **St-Germain-en-Laye**
            * Implémentation et automatisation de l'environnement de travail pour un projet interne
            * Programmation d'une application web au sein d'une équipe travaillant sous méthode Agile
        """)
        d_lines['alpha'][2].expander('`Python`, `Communication`, `État de l\'art`, ...').write("""
            Python · Git · Bash · Windows · Linux · Jupyter · Pandas · Django · Microsoft Azure · MySQL · 
            Docker · JIRA · Shell Scripting · Expressions régulières · Applications web · API REST · MongoDB
                      
            Développement front-end · Grattage de données · Algorithmes · Communication
            
            Méthodes agiles · DevOps
        """)
        
        d_lines['ins'][0].write(f"#### Doctorant en Neurosciences Computationnelles, {ins}")
        d_lines['ins'][1].markdown("""
            **4 ans** / *2013* / **Marseille**
            * Multistabilité dans la modélisation de l’activité cérébrale à large échelle
            * Analyses comparatives de séries temporelles entre patients épileptiques et contrôles
            * Développement de mon simulateur et outils pour les pré-traitements et analyses
        """)
        d_lines['ins'][2].expander('`Python`, `Recherche`, `État de l\'art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · k-means · PCA · ICA · 
            Seaborn · Shell Scripting · Expressions régulières · Plotly · Scikit-Learn · FCD · HPC
           
            Traitement du signal · Grattage de données · Analyse de données · Adaptation · Classification · Imagerie Médicale · 
            Algorithmes · Réseaux neuronaux · Machine Learning · Résolution de problèmes · Visualisation de données · 
            Recherche · Exploration des données · Nettoyage de données · Communication · Algèbre linéaire · État de l'art · 
            Modélisation mathématique · Méthode des éléments finis
            
            Indépendant · R&D
        """)
        
        d_lines['ins2'][0].write(f"#### Assistant Ingénieur, {ins}")
        d_lines['ins2'][1].markdown("""
            **9 mois** / *2013* / **Marseille**
            * Etude de modèles neuro-dynamiques pour la reconnaissance de configurations d'activité à l'état de repos (Resting-State Networks)
            * Création et étude d’un modèle dynamique pour publication
            * Apprentissage automatique de configurations d’activité
            * Création d'algorithmes d'apprentissage
        """)
        d_lines['ins2'][2].expander('`Python`, `Recherche`, `État de l\'art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · PCA · ICA · 
            Shell Scripting · Expressions régulières · Scikit-Learn · HPC
           
            Traitement du signal · Analyse de données · Adaptation · Classification · Algorithmes · Réseaux neuronaux · 
            Résolution de problèmes · Visualisation de données · Recherche · Exploration des données · Nettoyage de données · 
            Communication · Algèbre linéaire · État de l'art · Modélisation mathématique · Méthode des éléments finis · Pattern Recognition
            
            Indépendant · R&D
        """)
    
    
    elif sss['language'] == "en":
        header.header("Experiences", anchor='experiences', divider="orange")
        
        d_lines['jl'][0].write(f"#### Data Scientist, {jl}")
        d_lines['jl'][1].markdown("""
            **1 year** / *2023* / **Lille, France**
            * Recognition of animal behaviour
            * Cleaning, checking and analysing the data
            * Development, maintenance and optimization of algorithms, pipelines and APIs
        """)
        d_lines['jl'][2].expander('`Python`, `Time Series`, `Kubernetes`, ...').write("""
            Python · Git · Plotly · Bash · Linux · Windows · Jupyter · Pandas · Scikit-Learn · 
            Docker · Seaborn · Kubernetes · Notion · Shell Scripting · Regular expressions · Web applications · 
            Scaleway · Matplotlib · API REST
            
            Webscrapping · Data Analysis · Signal processing · Machine learning · 
            Natural Language Processing · Numerical Simulation · Classification · 
            Scientific analysis · Algorithmes · Regression modelling · Data cleaning · 
            Time Series · Problem solving · Data Visualization · Data exploration
            
            Agiles methods · R&D · DevOps · Independant
        """)
        
        d_lines['lindera'][0].write(f"#### Data Scientist Clinical, {lindera}")
        d_lines['lindera'][1].markdown("""
            **2 months** / *2023* / **Italy and Germany**
            * Intermediate between the Clinical and Data Science teams
            * Cleaning / Checking / Analysing the data
            * Code Refactoring / Optimization
        """)
        d_lines['lindera'][2].expander('`Python`, `Unstructured data`, `Liaison agent`, ...').write("""
            Python · Git · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Microsoft Excel
           
            Data Analysis · Adaptation · Unstructured data · Deep Learning · Problem solving · 
            Data Visualization · Research · Data exploration · Data cleaning
            
            Agiles methods · Liaison agent
        """)
        
        d_lines['xrator'][0].write(f"#### Data Scientist, {xrator}")
        d_lines['xrator'][1].markdown("""
            **9 months** / *2022* / **France and Vietnam**
            * Improve Cyber Risk Management and Reporting for IT or CISO
            * Study, Extract, Clean, Manage and Analyze the data
            * Identify gaps and use data for risk quantification
            * Creation/Refactoring/Optimization of code to process the data
            * Studying the state of the art for imputation and classification
        """)
        d_lines['xrator'][2].expander('`Python`, `Unstructured data`, `NLP`, ...').write("""
            Python · Git · GitLab · Matplotlib · Bash · Linux · Windows · Jupyter · Pandas · Django · 
            Docker · Seaborn · Kubernetes · OVH · Shell Scripting · Regular expressions · Web applications · 
            API REST · Prefect · NLTK · Spacy · JIRA · AWS · PyTorch · Plotly · Microsoft Azure · MySQL · 
            Scikit-Learn · NoSQL
           
            Webscrapping · Natural Language Processing · Data Analysis · Adaptation · 
            Unstructured data · Imputation · Regression modelling · Classification · Algorithmes · 
            Machine Learning · Deep Learning · Transfert Learning · Problem solving · Partitioning · 
            Data visualization · Research · Data exploration · Data cleaning
            
            Agiles methods · R&D · DevOps · Independant
        """)
        
        d_lines['oc'][0].write(f"#### Machine Learning Engineer (Internship), {oc}")
        d_lines['oc'][1].markdown("""
            **8 month** / *2021* / **Lille, France**  
            Mentored projects (weekly) including Data Cleaning and Data Analysis :
            * Produce an application for automatic multi-tagging of questions using state of the art algorithms (NLP, XMC, Deep Learning) 
            * Produce an application for race recognition of dog images (Deep Learning, Transfer Learning)
            * Segment customers of an e-commerce website (Unsupervised Learning, KMeans, HCA, DBSCAN)
            * Anticipate a city's electricity consumption and CO² emissions (Supervised Learning, SVM, Random Forest, Boosting, ...)
            * Design of an application on nutritional data for public health
        """)
        d_lines['oc'][2].expander('`Python`, `Communication`, `State of the art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · Django · Kaggle · k-means · Random forest · 
            Boosting · Docker · Seaborn · Shell Scripting · Regular expressions · Web applications · HCA · SVM · 
            API REST · NLTK · AWS · PyTorch · Plotly · MySQL · Scikit-Learn · TensorFlow · XMC · DBSCAN
           
            Webscrapping · Natural Language Processing · Data Analysis · Adaptation · 
            Unstructured data · Imputation · Regression modelling · Classification · Algorithmes · 
            Machine Learning · Deep Learning · Transfert Learning · Problem solving · Partitioning · 
            Data visualization · Research · Data exploration · Data cleaning · Neural Networks · 
            Inverse Problems · Image processing · Communication · Linear algebra · State of the art
            
            Independant
        """)
        
        d_lines['alpha'][0].write(f"#### DevOps Engineer, {alpha}")
        d_lines['alpha'][1].markdown("""
            **7 months** / *2019* / **Paris, France**
            * Implementing and automation of the coding environment for an internal project
            * Coding a web application within a team with Agile method
        """)
        d_lines['alpha'][2].expander('`Python`, `Communication`, `État de l\'art`, ...').write("""
            Python · Git · Bash · Windows · Linux · Jupyter · Pandas · Django · Microsoft Azure · MySQL · 
            Docker · JIRA · Shell Scripting · Regular expressions · Web applications · API REST · MongoDB
                      
            Développement front-end · Webscrapping · Algorithmes · Communication
            
            Agiles methods · DevOps
        """)
        
        d_lines['ins'][0].write(f"#### PhD Candidate in Computational Neurosciences, {ins}")
        d_lines['ins'][1].markdown("""
            **4 years** / *2013* / **Marseille, France**
            * Multistability in large scale of brain activity modeling
            * Comparative analyzes using functional connectivity dynamic between epileptic patients and controls
            * Developing my own simulator, preprocessing/analyzing tools in Python and its scientific libraries
        """)
        d_lines['ins'][2].expander('`Python`, `Research`, `État de l\'art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · Pandas · k-means · PCA · ICA · 
            Seaborn · Shell Scripting · Regular expressions · Plotly · Scikit-Learn · FCD · HPC
           
            Signal processing · Webscrapping · Data Analysis · Adaptation · Classification · Medical imaging · 
            Algorithmes · Neural networks · Machine Learning · Problem solving · Data visualization · 
            Research · Data exploration · Data cleaning · Communication · Linear algebra · State of the art · 
            Mathematical modelling · Finite element method · Time series
            
            Independant · R&D
        """)
        
        d_lines['ins2'][0].write(f"#### Assistant Engineer, {ins}")
        d_lines['ins2'][1].markdown("""
            **9 months** / *2013* / **Marseille, France**
            * Study of neuro-dynamic models for the recognition of activity configurations in the resting state (Resting-State Networks)
            * Creation and study of a dynamic model for publication
            * Machine learning of activity configurations
            * Creation of learning algorithms
        """)
        d_lines['ins2'][2].expander('`Python`, `Research`, `État de l\'art`, ...').write("""
            Python · Git · Matplotlib · Bash · Windows · Jupyter · PCA · ICA · 
            Shell Scripting · Regular expressions · Scikit-Learn · HPC
           
            Signal processing · Data Analysis · Adaptation · Classification · Algorithmes · Neural networks · 
            Problem solving · Data visualization · Research · Data exploration · Data cleaning · 
            Communication · Linear algebra · State of the art · Mathematical modelling · Finite element method · 
            Pattern Recognition · Time series
            
            Independant · R&D
        """)


if __name__ == "__main__":
    utils.always()
    main()
