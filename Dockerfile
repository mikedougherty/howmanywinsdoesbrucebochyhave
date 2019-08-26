FROM python:3.7-slim

# Image settings
WORKDIR /app
EXPOSE 5000
CMD ["pipenv", "run", "gunicorn", "-c", "config/gunicorn.py", "-b", "0.0.0.0:5000", "howmanywinsdoesbrucebochyhave:app"]

# Configure and install dependencies
RUN pip install -U pip pipenv tox setuptools

COPY Pipfile Pipfile.lock /app/
RUN pipenv install --dev

# Add project source
COPY . /app

RUN pipenv run python setup.py install && pipenv run tox
