FROM python:3.11-alpine

# Instalación de dependencias
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add nano
RUN pip install -r /requirements.txt
RUN pip install uWSGI
RUN apk del .tmp

#Gestión de directorios
RUN mkdir /powermeter
RUN mkdir -p /powermeter/static
COPY ./powermeter /powermeter
WORKDIR /powermeter

# Gestión de permisos de lectura/escritura
RUN adduser -D user
RUN chmod -R 777 /powermeter
USER user

# Crear archivos estáticos
RUN python manage.py collectstatic --noinput

CMD ["uwsgi", "--socket",":8000", "--master", "--enable-threads", "--module", "powermeter.wsgi"]
