FROM mysql/mysql-server:latest

ENV MYSQL_DATABASE lugdnd

COPY ./build_db.sql /docker-entrypoint-initdb.d/
#COPY starter_data.sql /docker-entrypoint-initdb.d/