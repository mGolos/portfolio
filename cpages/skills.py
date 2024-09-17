import streamlit as st
from tools import utils
sss = st.session_state


def main():
    dico = {
        (
                "📝 **Programming / Collaboration**",
                "📝 **Programmation / Collaboration**",
            ): {
            ("Languages", "Langages"): "`Python, SQL, Bash, Shell, MATLAB`",
            ("Environments", "Environnements"): "`VS Code, Jupyter Notebooks, Deepnote, Google Colab, Kaggle, Python Anywhere`",
            ("Package Management", "Gestion des Packages"): "`Pip, Anaconda, Virtualenv`",
            ("Testing Frameworks", "Frameworks de Test"): "`PyTest, Unittest`",
            ("Version Control", "Contrôle de Version"): "`Git, GitHub, GitLab, Bitbucket`",
            ("Collaboration Tools", "Outils de Collaboration"): "`Jira, Trello, Slack, Teams, Markdown, Confluence, Office, LaTeX`",
            ("Operating System", "Système d'exploitation"): "`Windows, Linux (Debian, CentOs, Ubuntu), macOS`",
        },
        (
                "📊 **Analysis / Data Visualization**",
                "📊 **Analyse / Visualisation de données**",
            ): {
            ("Python", "Python"): "`Pandas, NumPy, Matplotlib, Seaborn, Plotly`",
            ("Excel", "Excel"): "`Advanced Functions, Pivot Tables, VBA`",
            ("BI Tools", "Outils BI"): "`Tableau, Power BI, Dash, Streamlit, Xmind, Gephi`",
            ("Significance Testing", "Test de Signification"): "`dummy, baseline, a priori, p-values, Confidence Intervals`",
            ("Hypothesis Testing", "Test d'Hypothèse"): "`t-tests, ANOVA, Chi-Square Test`",
            ("Statistical Modeling", "Modélisation Statistique"): "`Time Series Analysis, Bayesian Inference, Regression, Probability Distributions`",
            ("Wrangling & Cleaning", "Nettoyage et Transformation"): "`Missing data handling, Outliers, Feature engineering, PCA, UMAP`",
            ("Model Evaluation", "Évaluation de Modèle"): "`Cross-validation, Confusion Matrix, ROC-AUC, Precision-Recall, F1 Score`",
        },
        (
                "🤖 **Machine Learning / NLP**",
                "🤖 **Machine Learning / NLP**",
            ): {
            ("Frameworks", "Frameworks"): "`Scikit-learn, TensorFlow, Keras, PyTorch`",
            ("Libraries", "Bibliothèques"): "`NLTK, SpaCy, Hugging Face Transformers, PIL, Scikit-image, BeautifulSoup`",
            ("Supervised Learning", "Apprentissage Supervisé"): "`Linear Regression, Logistic Regression, SVMs, Decision Trees, Random Forests, k-NN`",
            ("Unsupervised Learning", "Apprentissage Non Supervisé"): "`K-Means, PCA, DBSCAN`",
            ("Deep Learning", "Apprentissage Profond"): "`Neural Networks, CNNs, RNNs, Transfer Learning`",
            ("Text Processing", "Traitement de Texte"): "`Tokenization, Lemmatization, Stemming, Stopword Removal, Word2Vec`",
            ("Model Tuning", "Ajustement de Modèle"): "`Grid Search, Random Search, Hyperparameter Optimization, TPOT`",
            ("Optimization Methods", "Méthodes d'Optimisation"): "`Gradient Descent, Genetic Algorithms`",
        },
        (
                "🛠️ **DevOps / Data Engineering / Deployment**",
                "🛠️ **DevOps / Data Engineering / Déploiement**",
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
            * Problem identification & Functional needs analysis
            * Solution planning
            * Exploratory analysis & Conceptual and analytical vision
            * Data modeling and transformation for exploitation
            * Creation of tools for data processing and visualizations
            * Resolution of complex business problems
            * Application of state-of-the-art in the field
            * Critical thinking and scientific rigor
            * Ensuring responsibility for one or more functional processes
            """,
            """
            * Identification des problèmes & Analyse fonctionnelle des besoins
            * Planification des solutions
            * Analyse exploratoire & Vision analytique et conceptuelle
            * Modélisation et transformation des données pour exploitation
            * Création d’outils de traitements de données et de visualisations
            * Résolution de problématiques métiers complexes
            * Application de l’état de l’art du domaine
            * Raisonnement critique et rigueur scientifique
            * Assurer la responsabilité d'un ou plusieurs processus fonctionnels
            """),
    }

    st.header(
        "Compétences" if sss["lg_key"] else 'Hard Skills', 
        anchor='skills', divider="orange")
        
    for exp, sub in dico.items():
        with st.expander(exp[sss["lg_key"]], expanded=False):
            for k, v in sub.items():
                if sss['layout'] == "wide":
                    st.write(" : ".join([k[sss["lg_key"]], v]))
                else:
                    cs = st.columns([1,3])
                    cs[0].write(k[sss["lg_key"]])
                    cs[1].write(v)
    
    with st.expander(func_skills['name'][sss["lg_key"]], expanded=False):
        st.write(func_skills['description'][sss["lg_key"]])
    

if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
