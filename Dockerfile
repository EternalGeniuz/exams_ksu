FROM python:3.7
WORKDIR /app
COPY ./calculator.py .
ENTRYPOINT ["python", "calculator.py"]
