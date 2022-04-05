FROM postgres

COPY init.sql /docker-entrypoint-initdb.d/
#ENV POSTGRES_USER my_user
ENV POSTGRES_PASSWORD password
#ENV POSTGRES_DB user_db
#ENV POSTGRES_DB book_db
#ENV POSTGRES_DB issue_db
#ENV POSTGRES_MULTIPLE_DATABASES user_db, book_db, issue_db