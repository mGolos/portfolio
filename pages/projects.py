import utils
import streamlit as st
sss = st.session_state


def main():
    streamlit = "[Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)"
    link1 = "[Notebooks](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/question_tagging)"
    link2 = f"[!{streamlit}](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=question-tagging)"
    link3 = "[Notebooks](https://github.com/mGolos/Machine-Learning-Examples/tree/master/examples/breed_classifier)"
    link4 = f"[!{streamlit}](https://share.streamlit.io/mgolos/machine-learning-examples/main.py?p=breed-classifier)"

    if sss['language'] == "fr":
        st.markdown(f"""
            # Projets"""
            # f"""* Question Tagging ({link1}, {link2}) :  
            #     Production d'une application pour l'automatisation d'étiquetage multiple de questions en utilisant les algorithmes les plus récents/performants.  
            #     `[ État de l'art / NLP / XMC / Deep Learning ]`
            # * Breed Classifier ({link3}, {link4}) :  
            #     Production d'une application de reconnaissance de race d'images de chiens.  
            #     `[ Deep Learning / Transfert Learning ]`
            # * Segmentation de clients d'un site e-commerce.  
            #     `[ k-means / HCA / DBSCAN ]`
            # * Anticipation de la consommation électrique et émissions CO² d'une ville.  
            #     `[ SVM / Forêt aléatoires / Boosting ]`
            # * Conception d'une application sur des données nutritionnelles.  
            # ---"""
            """---
            (Nettoyage en cours)
        """)

    elif sss['language'] == "en":
        st.markdown(f"""
            # Projects"""
            # f"""* Question Tagging ({link1}, {link2}):  
            #     Produce an application for automatic multi-tagging of questions using state of the art algorithms.  
            #     `[ SOTA / NLP / XMC / Deep Learning ]`
            # * Breed Classifier ({link3}, {link4}):               
            #     Produce an application for race recognition of dog images.  
            #     `[ Deep Learning / Transfert Learning ]`
            # * Segmenting customers of an e-commerce website.  
            #     `[ k-means / HCA / DBSCAN ]`
            # * Anticipating a city's electricity consumption and CO² emissions.  
            #     `[ SVM / Random Forest / Boosting ]`
            # * Design of an application on nutritional data for public health.  
            # ---"""
            """
            (Cleaning in progress)
        """)


if __name__ == "__main__":
    utils.always()
    main()
