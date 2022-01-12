FROM certbot/certbot

ARG router_container_name

RUN apk update && apk add --no-cache docker-cli bash
COPY certbot/entrypoint.sh /usr/local/bin
RUN sed -i -r "s/ROUTER_CONTAINER_NAME_PLACEHOLDER/${router_container_name}/g" /usr/local/bin/entrypoint.sh

ENTRYPOINT [ "entrypoint.sh" ]
