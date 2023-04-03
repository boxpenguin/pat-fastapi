# Dockerimage file to build pat-fastapi
FROM python:3.10
WORKDIR /code
COPY ./Pipfile* /code/
COPY ./*.py /code/
RUN pip install pipenv
RUN pipenv update
# CMD ["/code/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
CMD uvicorn main:app --host 0.0.0.0 --port 8080