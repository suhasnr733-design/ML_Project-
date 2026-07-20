# Use a stable Python runtime
FROM python:3.12-slim

WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and model assets
COPY app.py ./
COPY RFmodel.pkl ./
COPY home_anime.json ./
COPY loading_anime.json ./
COPY icons ./icons

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
