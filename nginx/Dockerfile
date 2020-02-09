FROM nginx:stable-alpine
LABEL maintainer="Вадим Бажов: master@remort.net"

ARG server_name
ARG env

RUN apk --no-cache add --update bash && \
    find /etc/nginx/* ! -name 'mime.types' -delete && \
    rm -r /usr/share/nginx/html/* && \
    mkdir -p /var/www/webroot && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/${env}.conf /etc/nginx/server.conf
COPY nginx/ssl-dhparams.pem /etc/nginx/conf.d/ssl-dhparams.pem
COPY build/ /var/www/webroot/

RUN sed -i -r "s/DOMAIN_PLACEHOLDER/${server_name}/g" /etc/nginx/server.conf
