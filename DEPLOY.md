Deployment options

1) Streamlit Community Cloud
- Go to https://share.streamlit.io and sign in with your GitHub account.
- Create a new app and select your repository and branch (e.g., `main`).
- Set the main file to `app.py` and the requirements file to `requirements.txt`.
- Add any secrets (none required for basic usage). Streamlit will build and deploy automatically.

2) Render (container or Git)
- Option A: Use Render's GitHub integration (recommended). Connect your repo to Render, select the service type `Web Service`, set the start command `streamlit run app.py`, and point to the branch.
- Option B: Container deploy. The repository contains a `Dockerfile`. You can build and push a container to Render's private registry or Docker Hub and configure the service to use that image.
- The provided GitHub Action `.github/workflows/deploy-to-render.yml` can be used to trigger Render deploys when you set the following repo secrets:
  - `RENDER_API_KEY` — your Render account API key
  - `RENDER_SERVICE_ID` — the Render service id for your web service

3) Heroku / other hosts
- Use the `Procfile` and `requirements.txt` to deploy to Heroku. Upload `RFmodel.pkl` as a repository file or store it in an external object store.

Security note
- Do not commit secrets to the repo. Use GitHub repository secrets for API keys and service IDs.
