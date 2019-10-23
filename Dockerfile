FROM kennethreitz/pipenv:latest

EXPOSE 5000
WORKDIR /api/

COPY ./Pipfile ./Pipfile.lock /api/
COPY ./api /api/

RUN pipenv --python 3.7 && pipenv install --dev

CMD ["pipenv", "run", "gunicorn", "-c", "gunicorn.ini", "wsgi:app"]