# app/Dockerfile

FROM python:3.12-slim

WORKDIR /app
COPY app/ ./app/
COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

ARG PORT=8501
ENV PORT=${PORT}

EXPOSE $PORT

HEALTHCHECK CMD curl --fail http://localhost:$PORT/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]