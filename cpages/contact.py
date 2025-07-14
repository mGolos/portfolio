import streamlit as st
from streamlit_image_comparison import image_comparison
from tools import utils
sss = st.session_state


def main():
    contact = """
        :globe_with_meridians: [LinkedIn](https://www.linkedin.com/in/mathieu-golos-25055b77/) / [Malt](https://www.malt.fr/profile/mathieugolos)  
        :email: [mathieu.golos@gmail.com](mail:mathieu.golos@gmail.com)  
        :telephone_receiver: [+33611478901](tel:+33611478901)  
        :earth_africa: [Lille (FRANCE)](https://goo.gl/maps/eXC8BJh9qGXWBgZDA)  
    """
    st.header("Contact", anchor='contact', divider="orange")
    
    if sss["language"] == "fr":
        st.markdown("""
            La meilleur façon de me joindre est par email.
        """)
    elif sss["language"] == "en":
        st.markdown("""
            The best way to contact me is by email.
        """)
    st.write(contact)


if __name__ == "__main__":
    utils.always()
    main()
    utils.background()
