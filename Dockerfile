FROM python:3.9.19-slim-bullseye
RUN apt update
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "ip_app.py"]
