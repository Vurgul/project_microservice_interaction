FROM python:3.9

WORKDIR .
COPY requirements.txt .
RUN pip install --upgrade pip install -r requirements.txt
COPY . .

CMD ["hupper", "-m", "waitress", "--port=8000", "--host=0.0.0.0", "user_service.composites.user_api:app"]