import streamlit as st
from tools import utils
sss = st.session_state


def main():
    dico = {
        (
                "⌨️ **Programming** 📝 **Collaboration**",
                "⌨️ **Programmation** 📝 **Collaboration**",
            ): {
            ("Languages", "Langages"): "`Python, SQL, Bash, Shell, MATLAB`",
            ("Environments", "Environnements"): "`VS Code, Jupyter Notebooks, Deepnote, Google Colab, Kaggle, Python Anywhere`",
            ("Package Management", "Gestion des Packages"): "`Pip, Conda, Virtualenv`",
            ("Testing Frameworks", "Frameworks de Test"): "`PyTest, Unittest`",
            ("Version Control", "Contrôle de Version"): "`Git, GitHub, GitLab, Bitbucket`",
            ("Collaboration Tools", "Outils de Collaboration"): "`Jira, Trello, Slack, MS Teams, Markdown, Confluence`",
        },
        (
                "🔍 **Analysis** 📊 **Data Visualization**",
                "🔍 **Analyse** 📊 **Visualisation de données**",
            ): {
            ("Python", "Python"): "`Pandas, NumPy, Matplotlib, Seaborn, Plotly`",
            ("Excel", "Excel"): "`Advanced Functions, Pivot Tables, VBA`",
            ("BI Tools", "Outils BI"): "`Tableau, Power BI, Dash, Streamlit`",
            ("Significance Testing", "Test de Signification"): "`dummy, baseline, a priori, p-values, Confidence Intervals`",
            ("Hypothesis Testing", "Test d'Hypothèse"): "`t-tests, ANOVA, Chi-Square Test`",
            ("Statistical Modeling", "Modélisation Statistique"): "`Time Series Analysis, Bayesian Inference, Regression, Probability Distributions`",
            ("Wrangling & Cleaning", "Nettoyage et Transformation"): "`Missing data handling, Outliers, Feature engineering, PCA, UMAP`",
            ("Model Evaluation", "Évaluation de Modèle"): "`Cross-validation, Confusion Matrix, ROC-AUC, Precision-Recall, F1 Score`",
        },
        (
                "🤖 **Machine Learning** 💬 **NLP**",
                "🤖 **Machine Learning** 💬 **NLP**",
            ): {
            ("Frameworks", "Frameworks"): "`Scikit-learn, TensorFlow, Keras, PyTorch`",
            ("Libraries", "Bibliothèques"): "`NLTK, SpaCy, Hugging Face Transformers, PIL, Scikit-image`",
            ("Supervised Learning", "Apprentissage Supervisé"): "`Linear Regression, Logistic Regression, SVMs, Decision Trees, Random Forests, k-NN`",
            ("Unsupervised Learning", "Apprentissage Non Supervisé"): "`K-Means, PCA, DBSCAN`",
            ("Deep Learning", "Apprentissage Profond"): "`Neural Networks, CNNs, RNNs, Transfer Learning`",
            ("Text Processing", "Traitement de Texte"): "`Tokenization, Lemmatization, Stemming, Stopword Removal, Word2Vec`",
            ("Model Tuning", "Ajustement de Modèle"): "`Grid Search, Random Search, Hyperparameter Optimization, TPOT`",
            ("Optimization Methods", "Méthodes d'Optimisation"): "`Gradient Descent, Genetic Algorithms`",
        },
        (
                "🛠️ **DevOps / Data Engineering** ☁️ **Deployment**",
                "🛠️ **DevOps / Data Engineering** ☁️ **Déploiement**",
            ): {
            ("APIs for Deployment", "APIs pour Déploiement"): "`Flask, FastAPI, Django REST Framework`",
            ("CI/CD", "CI/CD"): "`GitLab CI, GitHub Actions, Jenkins`",
            ("Cloud Platforms", "Plateformes Cloud"): "`AWS, GCP, Microsoft Azure`",
            ("Containerization & Orchestration", "Containerisation & Orchestration"): "`Docker, Kubernetes, Prefect`",
            ("Serverless", "Serverless"): "`AWS Lambda, Google Cloud Functions, Azure Functions`",
            ("Databases", "Bases de Données"): "`MySQL, PostgreSQL, SQLite, MongoDB, Redis`",
            ("Monitoring", "Surveillance"): "`Prometheus, Grafana, MLFlow`",
        },
    }
    func_skills = {
        "name": (
            "🧩 **Functional Skills**",
            "🧩 **Compétences Fonctionnelles**"),
        "description": (
            """
            * Functional analysis of clients needs
            * Data transformation into usable form
            * Resolution of complex business problems
            * Analytical and conceptual vision
            * Responsible for one or more functional processes
            * Application of state-of-the-art knowledge in the field
            * Creation of data processing tools and visualizations
            * Signal processing
            * Critical reasoning and scientific methodology
            """,
            """
            * Analyse fonctionnelle des besoins clients
            * Transformation des données en exploitable
            * Résolution des problématiques métiers complexe
            * Vision analytique et conceptuelle
            * Assurer la responsabilité d'un ou plusieurs processus fonctionnels
            * Application de l’état de l’art du domaine
            * Création d’outils de traitements de données et de visualisations
            * Traitement du signal
            * Raisonnement critique et méthodologie scientifique
            """),
    }

    st.header(
        "Compétences" if sss["lg_key"] else 'Hard Skills', 
        anchor='education', divider="orange")
        
    for exp, sub in dico.items():
        with st.expander(exp[sss["lg_key"]], expanded=True):
            for k, v in sub.items():
                if sss['layout'] == "wide":
                    st.write(" : ".join([k[sss["lg_key"]], v]))
                else:
                    cs = st.columns([1,3])
                    cs[0].write(k[sss["lg_key"]])
                    cs[1].write(v)
    
    with st.expander(func_skills['name'][sss["lg_key"]], expanded=True):
        st.write(func_skills['description'][sss["lg_key"]])
    

if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
