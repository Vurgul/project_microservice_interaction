FROM python:3.7-slim

WORKDIR /app
#COPY requirements.txt .
#RUN pip install --upgrade pip && pip install -r requirements.txt
COPY setup.cfg .
COPY setup.py .
RUN pip install --upgrade pip && pip install -e ".[dev]"
COPY . .

# CMD ["hupper", "-m", "waitress", "--port=2222", "--host=0.0.0.0", "book_service.composites.book_api:app"]
CMD ["gunicorn", "-b", "0.0.0.0:2222", "book_service.composites.book_api:app", "--reload"]
# gunicorn -b 0.0.0.0:2222 book_service.composites.book_api:app --reload
# hupper -m waitress --port=8000 --host=127.0.0.1 book_service.composites.book_api:app
