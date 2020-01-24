FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

RUN apt install -y git
RUN python -m pip install --upgrade pip
RUN pip install git+https://github.com/gunthercox/chatterbot-corpus.git#egg=chatterbot-corpus
RUN pip install  -r requirements.txt --no-cache-dir

