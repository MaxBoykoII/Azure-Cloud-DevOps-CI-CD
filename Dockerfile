FROM python:3.9.0-slim-buster

WORKDIR /usr/src/app

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevent Python from buffering stdout and stderrr
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py run -h 0.0.0.0