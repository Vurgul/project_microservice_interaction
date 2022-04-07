FROM python:3.7-slim

WORKDIR /app

COPY setup.cfg .
COPY setup.py .
RUN pip install --upgrade pip && pip install -e ".[dev]"
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:3333", "issue_service.composites.issue_api:app", "--reload"]

