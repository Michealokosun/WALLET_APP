#!/usr/bin/env python 
"""Contains the database connection and all communication with the database"""
import psycopg2

params = {"host" :"localhost",
          "port" : 5432,
        "database" : "WALLET_APP",
        "user" :"postgres",
        "password": "****"}


def connect(config):
    """
    Connects to a PostgreSQL database using the provided configuration.

    Prints a message indicating whether the connection was successful.
    Returns the database connection object on success."""
    try:
        # connecting to the PostgreSQL server        
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

connect(params)