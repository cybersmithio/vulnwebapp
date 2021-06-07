FROM python:3.8

RUN apt-get update && apt-get
COPY requirements.txt vulnwebapp.py ./
RUN pip install --upgrade -vvv pip
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir templates static
COPY templates/ ./templates/
COPY static/ ./static/

ENV FLASK_APP=vulnwebapp
RUN apt update

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]
