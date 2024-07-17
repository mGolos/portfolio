import utils
import streamlit as st
from streamlit_timeline import timeline
sss = st.session_state


# @st.cache_data
def load_json(lang: str):
    assert lang in {'fr', 'en'}
    with open(f'data/timeline_{lang}.json', "r") as f:
        return f.read()


# @st.cache_resource
def main(): 
    
    st.markdown('<img src="file://images/photo2.jpg" />', unsafe_allow_html=True)
    st.markdown('<img src="data:image/jpg;base64,/images/photo2.jpg" />', unsafe_allow_html=True)

    if sss["language"] == "fr":
        st.markdown("# Chronologie")

    elif sss["language"] == "en":
        st.markdown("# Timeline")
    
    data = load_json(sss["language"])
    timeline(data, height=800)


if __name__ == "__main__":
    utils.always()
    main()
