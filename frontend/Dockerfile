FROM nginx

COPY index.html /usr/share/nginx/html

RUN mkdir /etc/nginx/templates

COPY frontend/default.conf.template /etc/nginx/templates/
