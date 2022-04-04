FROM postgres

COPY init.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD root
# ENV POSTGRES_DB user_db
