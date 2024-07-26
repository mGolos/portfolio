import pages
import importlib
import streamlit as st
from tools import utils
sss = st.session_state


if __name__ == "__main__":
    utils.always()
    
    pages = [
        'about', 'experiences', 'education', 'projects', 'skills', 
        'publications', 'cv', 'recommendations']
    for page in pages:
        submodule = importlib.import_module(f'pages.{page}')
        submodule.main()
    
    utils.footer()
    utils.background()
