import streamlit as st
from tools import utils
sss = st.session_state


def main():
    dico = {
        (":keyboard: **Programmation & Collaboration**", ":keyboard: **Programming & Collaboration**"): {
            ("Langages", "Languages"): "`Python, SQL, Bash, Shell, MATLAB`",
            ("Environnements", "Environments"): "`VS Code, Jupyter Notebooks, Deepnote, Google Colab, Kaggle, Python Anywhere`",
            ("Gestion des Packages", "Package Management"): "`Pip, Conda, Virtualenv`",
            ("Frameworks de Test", "Testing Frameworks"): "`PyTest, Unittest`",
            ("Contrôle de Version", "Version Control"): "`Git, GitHub, GitLab, Bitbucket`",
            ("Outils de Collaboration", "Collaboration Tools"): "`Jira, Trello, Slack, MS Teams, Markdown, Confluence`",
        },
        (":bar_chart: **Analyse & Visualisation de données**", ":bar_chart: **Analysis & Data Visualization**"): {
            ("Python", "Python"): "`Pandas, NumPy, Matplotlib, Seaborn, Plotly`",
            ("Excel", "Excel"): "`Advanced Functions, Pivot Tables, VBA`",
            ("Outils BI", "BI Tools"): "`Tableau, Power BI, Dash, Streamlit`",
            ("Test de Signification", "Significance Testing"): "`dummy, baseline, a priori, p-values, Confidence Intervals`",
            ("Test d'Hypothèse", "Hypothesis Testing"): "`t-tests, ANOVA, Chi-Square Test`",
            ("Modélisation Statistique", "Statistical Modeling"): "`Time Series Analysis, Bayesian Inference, Regression, Probability Distributions`",
            ("Nettoyage et Transformation", "Wrangling & Cleaning"): "`Missing data handling, Outliers, Feature engineering, PCA, UMAP`",
            ("Évaluation de Modèle", "Model Evaluation"): "`Cross-validation, Confusion Matrix, ROC-AUC, Precision-Recall, F1 Score`",
        },
        (":robot_face: **Machine Learning & NLP**", ":robot_face: **Machine Learning & NLP**"): {
            ("Frameworks", "Frameworks"): "`Scikit-learn, TensorFlow, Keras, PyTorch`",
            ("Bibliothèques", "Libraries"): "`NLTK, SpaCy, Hugging Face Transformers, PIL, Scikit-image`",
            ("Apprentissage Supervisé", "Supervised Learning"): "`Linear Regression, Logistic Regression, SVMs, Decision Trees, Random Forests, k-NN`",
            ("Apprentissage Non Supervisé", "Unsupervised Learning"): "`K-Means, PCA, DBSCAN`",
            ("Apprentissage Profond", "Deep Learning"): "`Neural Networks, CNNs, RNNs, Transfer Learning`",
            ("Traitement de Texte", "Text Processing"): "`Tokenization, Lemmatization, Stemming, Stopword Removal, Word2Vec`",
            ("Ajustement de Modèle", "Model Tuning"): "`Grid Search, Random Search, Hyperparameter Optimization, TPOT`",
            ("Méthodes d'Optimisation", "Optimization Methods"): "`Gradient Descent, Genetic Algorithms`",
        },
        (":hammer_and_wrench: **DevOps, Data Engineering & Deploiement**", ":hammer_and_wrench: **DevOps, Data Engineering & Model Deployment**"): {
            ("APIs pour Déploiement", "APIs for Deployment"): "`Flask, FastAPI, Django REST Framework`",
            ("CI/CD", "CI/CD"): "`GitLab CI, GitHub Actions, Jenkins`",
            ("Plateformes Cloud", "Cloud Platforms"): "`AWS, GCP, Microsoft Azure`",
            ("Containerisation & Orchestration", "Containerization & Orchestration"): "`Docker, Kubernetes, Prefect`",
            ("Serverless", "Serverless"): "`AWS Lambda, Google Cloud Functions, Azure Functions`",
            ("Bases de Données", "Databases"): "`MySQL, PostgreSQL, SQLite, MongoDB, Redis`",
            ("Surveillance", "Monitoring"): "`Prometheus, Grafana, MLFlow`",
        },
    }
    
    if sss['language'] == "fr":
        st.header("Compétences", anchor='skills', divider="orange")
        lg_key = 0
        lg_str_join = ' : '

    elif sss['language'] == "en":
        st.header("Hard Skills", anchor='skills', divider="orange")
        lg_key = 1
        lg_str_join = ': '
        
    for exp, sub in dico.items():
        with st.expander(exp[lg_key], expanded=True):
            for k, v in sub.items():
                if sss['layout'] == "wide":
                    st.write(lg_str_join.join([k[lg_key], v]))
                else:
                    cs = st.columns([1,3])
                    cs[0].write(k[lg_key])
                    cs[1].write(v)


if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
