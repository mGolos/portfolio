[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mgolos/portfolio/main/main.py)

# Running localy
* Create: `conda create --name portfolio python=3.11.0`
* Activate: `conda activate portfolio`
* Install libraries from pip: `pip install -r requirements.txt`
* Running: `streamlit run app.py`

# Uninstalling
* Deactivate: `conda deactivate`
* Delete: `conda remove --name portfolio --all`

# Scaleway
1. Create secrets on the [IAM](https://console.scaleway.com/iam/api-keys)
    * for an App
    * configured for a project
    * get the secrets: `SCW_ACCESS_KEY`, `SCW_SECRET_KEY`, `SCW_DEFAULT_PROJECT_ID`
1. Create a [container namespace](https://console.scaleway.com/containers/namespaces/fr-par)
    In parameters of the namespace:
    * copy the `Endpoint du Registry` to `SCW_CONTAINER_NAMESPACE_REGISTRY_ENDPOINT`
1. Create deployment files
    * `Dockerfile`: be careful with the Python version and environment file
    * `.github/workflows/docker.yml`: put Scaleway variables here and in Github Actions Secrets
        - `SCW_ACCESS_KEY` (SCALEWAY_API_KEY)
        - `SCW_SECRET_KEY` (SCALEWAY_API_SECRET)
        - `SCW_DEFAULT_PROJECT_ID` (SCALEWAY_PROJECT_ID)
        - `SCW_CONTAINER_NAMESPACE_REGISTRY_ENDPOINT` (CONTAINER_REGISTRY_ENDPOINT)
        - `SCW_CONTAINER_ID`: get later after the first Action (that should fail)
1. Container ID
    1. Open the CLI (command shell) in Scaleway
    1. `scw container container list`
    1. Copy the ID of the built container
    1. Put it in Github Actions Secrets in `SCW_CONTAINER_ID`
1. Restart the Action