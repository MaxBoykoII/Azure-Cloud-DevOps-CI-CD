FROM python:3.7.3-stretch

WORKDIR /usr/src/app

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevent Python from buffering stdout and stderrr
ENV PYTHONUNBUFFERED 1

# Install make
RUN apt-get update && apt-get install make

COPY ./requirements.txt .
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY . .

CMD python manage.py run -h 0.0.0.0