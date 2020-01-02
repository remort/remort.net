FROM nginx:stable-alpine

ARG server_name
ARG env

RUN apk add --update bash && rm -rf /var/cache/apk/* && \
    find /etc/nginx/* ! -name 'mime.types' -delete && \
    rm -r /usr/share/nginx/html/* && \
    mkdir -p /opt/bin && \
    mkdir -p /var/www/remort.net && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx/nginx.${env}.conf /etc/nginx/nginx.conf
COPY build/ /var/www/webroot/

RUN sed -i -r "s/DOMAIN_PLACEHOLDER/${server_name}/g" /etc/nginx/nginx.conf
ADD https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf /etc/nginx/conf.d/options-ssl-nginx.conf
ADD https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem /etc/nginx/conf.d/ssl-dhparams.pem
