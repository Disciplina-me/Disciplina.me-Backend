#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE DATABASE disciplina_me_auth;
  CREATE DATABASE disciplina_me_calendar;
  CREATE DATABASE disciplina_me_subjects;
EOSQL
