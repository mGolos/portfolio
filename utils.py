import streamlit as st


def st_query_radio(label, param, options, key=None):
    key = f"st_query_radio.{key or param}"

    choice = st.experimental_get_query_params().get(param, ("",))[0]

    def on_change():
        params = st.experimental_get_query_params()
        params[param] = st.session_state[key]

        st.experimental_set_query_params(**params)

    names = {f.__name__: n for f,n in zip(options.values(), options.keys())}
    st.session_state[key] = choice if choice in names else next(iter(names))
    st.sidebar.radio(label, tuple(names.keys()), format_func=lambda x: names[x] , on_change=on_change, key=key)

    return [o for o in options.values() if o.__name__ == st.session_state[key]][0]