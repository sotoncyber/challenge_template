FROM python:3.10

RUN pip install poetry

COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock

WORKDIR /app

RUN poetry install --without dev

COPY . /app

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0", "challenge:app"]
