FROM python:3

RUN pip3 install mysql-connector-python

RUN mkdir /insert

COPY insert_data.py /insert/

RUN chmod +x /insert/insert_data.py

WORKDIR /insert/

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh

RUN chmod +x ./wait-for-it.sh

ENTRYPOINT [ "/bin/bash", "-c"]

CMD ["./wait-for-it.sh backend:5000 -s --timeout=100; python3 insert_data.py; echo done"]