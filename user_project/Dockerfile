FROM python:3.7-slim

WORKDIR /app

COPY setup.cfg .
COPY setup.py .
RUN pip install --upgrade pip && pip install -e ".[dev]"
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:1111", "user_service.composites.user_api:app", "--reload"]

