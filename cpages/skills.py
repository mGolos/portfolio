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
            ("Environments", "Environnements"): "`VS Code, Jupyter, Deepnote, Google Colab, Kaggle`",
            ("Package Management", "Gestion des Packages"): "`Pip, Anaconda, Virtualenv`",
            ("Testing Frameworks", "Frameworks de Test"): "`PyTest, Unittest`",
            ("Version Control", "Contrôle de Version"): "`Git, GitHub, GitLab, Bitbucket`",
            ("Collaboration", "Collaboration"): "`Jira, Trello, Slack, Teams, Confluence`",
            ("Operating System", "Système d'exploitation"): "`Windows, Linux`",
        },
        (
                "📊 **Analysis / Data Visualization**",
                "📊 **Analyse / Visualisation de données**",
            ): {
            ("Python", "Python"): "`Pandas, NumPy, Matplotlib, Seaborn, Plotly`",
            ("BI Tools", "Outils BI"): "`Tableau, Power BI, Dash, Streamlit, Drawio, Gephi`",
            ("Testing", "Tests"): "`t-tests, ANOVA, Chi-Square Test`",
            ("Statistics", "Statistique"): "`Time Series Analysis, Probability Distributions`",
            ("Preparation", "Préparation"): "`Data cleaning, Feature engineering`",
            ("Evaluation", "Évaluation"): "`Cross-validation, ROC-AUC, Precision-Recall`",
        },
        (
                "🤖 **Machine Learning / NLP**",
                "🤖 **Machine Learning / NLP**",
            ): {
            ("Frameworks", "Frameworks"): "`Scikit-learn, TensorFlow, Keras, PyTorch`",
            ("Libraries", "Bibliothèques"): "`NLTK, SpaCy, BeautifulSoup`",
            ("Supervised ML", "ML Supervisé"): "`Regression, Decision Trees, Random Forests`",
            ("Unsupervised ML", "ML Non Supervisé"): "`K-Means, PCA`",
            ("Deep Learning", "Deep Learning"): "`Neural Networks, CNNs, RNNs, Transfer Learning`",
            ("Text Processing", "Traitement de Texte"): "`Tokenization, Lemmatization`",
            ("Optimization", "Optimisation"): "`Gradient Descent, Genetic Algorithms`",
        },
        (
                "🛠️ **DevOps / Data Engineering / Deployment**",
                "🛠️ **DevOps / Data Engineering / Déploiement**",
            ): {
            ("APIs", "APIs"): "`Flask, FastAPI, Django`",
            ("CI/CD", "CI/CD"): "`GitLab CI, GitHub Actions, Jenkins`",
            ("Cloud", "Cloud"): "`Scaleway, Azure, AWS, GCP`",
            ("Orchestration", "Orchestration"): "`Docker, Kubernetes, Prefect`",
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
            * Identifying and analyzing needs
            * Planning and implementing solutions
            * Exploratory analysis and conceptual vision
            * Data modeling and transformation
            * Creating data visualization tools
            * Solving business problems
            * Applying industry best practices
            * Critical thinking and scientific rigor
            * Managing functional processes
            """,
            """
            * Identification et analyse des besoins
            * Planification et mise en oeuvre des solutions
            * Analyse exploratoire et vision conceptuelle
            * Modélisation et transformation des données
            * Création d'outils de traitement et visualisation
            * Résolution de problématiques métiers complexes
            * Application de l'état de l'art du domaine
            * Raisonnement critique et rigueur scientifique
            * Gestion de processus fonctionnels
            """),
    }

    st.header(
        "Compétences" if sss["lg_key"] else 'Hard Skills', 
        anchor='skills', divider="orange")
        
    for exp, sub in dico.items():
        with st.expander(exp[sss["lg_key"]], expanded=False):
            skills = []
            for k, v in sub.items():
                if sss['layout'] == "wide":
                    skills.append(" : ".join([k[sss["lg_key"]], v])  + "  ")
                    # st.write(" : ".join([k[sss["lg_key"]], v]))
                else:
                    cs = st.columns([1,3])
                    cs[0].write(k[sss["lg_key"]])
                    cs[1].write(v)
            if sss['layout'] == "wide":
                st.write("\n".join(skills))
    
    with st.expander(func_skills['name'][sss["lg_key"]], expanded=True):
        st.write(func_skills['description'][sss["lg_key"]])
    

if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
