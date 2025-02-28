#!/bin/bash

#psql -h 172.28.0.5 -U odoo -c "CREATE DATABASE electronicinvoice;"
psql -h 172.28.0.5 -U odoo -d electronicinvoice -c "CREATE TABLE users (
    id serial PRIMARY KEY,
    name varchar NOT NULL,
    email varchar NOT NULL,
    password varchar NOT NULL,
    nit varchar NOT NULL
);"