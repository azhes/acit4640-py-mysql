FROM python:3

RUN apt-get update -qy && apt-get install -y wait-for-it
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y default-mysql-client
RUN apt-get install -y gettext-base

COPY backend/app /app

RUN useradd -m -d /backend backend

RUN mv app/ /backend/src/

RUN chown -R backend /backend/src

RUN su - backend

RUN pip3 install --user -r /backend/src/requirements.txt

RUN pip3 install mysql-connector-python

COPY backend/app/backend.conf.template /backend/src/

WORKDIR /backend/src/

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh

RUN chmod +x ./wait-for-it.sh

ENV FLASK_APP=app
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD ["envsubst < backend.conf.template > backend.conf;./wait-for-it.sh database1:3306 -s --timeout=100; python3 -m flask run"]
