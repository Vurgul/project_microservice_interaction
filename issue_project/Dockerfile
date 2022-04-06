FROM python:3.7-slim

WORKDIR /app
#COPY requirements.txt .
#RUN pip install --upgrade pip && pip install -r requirements.txt
COPY setup.cfg .
COPY setup.py .
RUN pip install --upgrade pip && pip install -e ".[dev]"
COPY . .

# CMD ["hupper", "-m", "waitress", "--port=3333", "--host=0.0.0.0", "issue_service.composites.issue_api:app"]
CMD ["gunicorn", "-b", "0.0.0.0:3333", "issue_service.composites.issue_api:app", "--reload"]
# hupper -m waitress --port=8000 --host=127.0.0.1 issue_service.composites.issue_api:app
