FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements-prod.txt
COPY . .
CMD ["sh", "run.sh"]
