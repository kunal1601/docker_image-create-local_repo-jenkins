FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
