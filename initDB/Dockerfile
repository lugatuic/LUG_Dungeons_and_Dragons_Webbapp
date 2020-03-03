FROM mysql:5.7

ENV MYSQL_DATABASE lugdb

COPY ./build_db.sql /docker-entrypoint-initdb.d/
#COPY starter_data.sql /docker-entrypoint-initdb.d/
