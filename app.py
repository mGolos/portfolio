import pages
import utils
import importlib
import streamlit as st
sss = st.session_state


if __name__ == "__main__":
    utils.always()
    
    pages = [
        'about', 'journey', 'projects', 
        'skills', 'timeline',
        'publications', 'cv', 'recommendations']
    for page in pages:
        submodule = importlib.import_module(f'pages.{page}')
        submodule.main()
    
    utils.footer()
