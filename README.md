# Bengaluru House Price Predictor

A Streamlit app for estimating house prices in Bangalore using a trained Random Forest model.

**Live Demo**: [Open app on Streamlit Community Cloud](https://share.streamlit.io/suhasnr733-design/ML_Project-/main/app.py)

Badge: [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/suhasnr733-design/ML_Project-/main/app.py)

## Files

- `app.py` - main Streamlit application
- `RFmodel.pkl` - trained prediction model
- `requirements.txt` - Python dependencies
- `Dockerfile` - container deployment support
- `Procfile` - Heroku/Render-style deployment support
- `.github/workflows/deploy-streamlit.yml` - GitHub Actions smoke test workflow
 - `.github/workflows/deploy-to-render.yml` - GitHub Actions deploy template for Render
 - `.streamlit/config.toml` - Streamlit Cloud configuration

## Run locally

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Docker

```bash
docker build -t bangalore-price-predictor .
docker run -p 8501:8501 bangalore-price-predictor
```

## GitHub Actions

The workflow in `.github/workflows/deploy-streamlit.yml` validates the app on push to `main` or `master`.

There is also a deploy template at `.github/workflows/deploy-to-render.yml` that can trigger a Render deployment when you provide `RENDER_API_KEY` and `RENDER_SERVICE_ID` as repository secrets. See `DEPLOY.md` for full instructions.

## Notes

- Keep `RFmodel.pkl` and the dataset files in the repository for local deployment.
- For production use, consider storing files in a secure object store instead of the Git repo.
