# 1. Use official Python runtime
FROM python:3.10-slim

# 2. Install system deps (if any) and Ollama CLI
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://ollama.com/install.sh | bash && \
    rm -rf /var/lib/apt/lists/*

# 3. Copy your project & install Python deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# 4. Expose Flask port
EXPOSE 5000

# 5. Start Ollama and your Flask app
CMD ollama serve chatgpt4o-mini --listen 0.0.0.0:11434 & \
    python app.py
