FROM nginx:stable-alpine

ARG server_name
ARG env

RUN apk add --update bash && rm -rf /var/cache/apk/* && \
    find /etc/nginx/* ! -name 'mime.types' -delete && \
    rm -r /usr/share/nginx/html/* && \
    mkdir -p /var/www/webroot && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx/${env}.conf /etc/nginx/nginx.conf
COPY nginx/ssl-dhparams.pem /etc/nginx/conf.d/ssl-dhparams.pem
COPY build/ /var/www/webroot/

RUN sed -i -r "s/DOMAIN_PLACEHOLDER/${server_name}/g" /etc/nginx/nginx.conf
