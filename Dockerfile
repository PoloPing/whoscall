# Can not find mysqlclint:2.0.3 at brunneis/python:3.7.0-ubuntu-18.04
FROM python:3.7

# Set default WORKDIR in container
WORKDIR /usr/src/app

# Update the repository
COPY . .

# For log message in container
ENV PYTHONUNBUFFERED 1
# For flask app anem
ENV FLASK_APP "app.py"

# Update debian source
RUN echo deb http://ftp.tw.debian.org/debian/ stable main > /etc/apt/sources.list && \
    echo deb http://ftp.tw.debian.org/debian/ stable-updates main >> /etc/apt/sources.list && \
    echo deb http://security.debian.org/ stable/updates main  >> /etc/apt/sources.list && \
    echo deb http://ftp.debian.org/debian stretch-backports main  >> /etc/apt/sources.list

# Install package requirements
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# EXPOSE 80
EXPOSE 80

# Start point
CMD "flask run --host=0.0.0.0 --port=80"]


