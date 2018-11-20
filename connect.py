import psycopg2

import urllib.parse as urlparse

import os

user = urlparse.urlparse(os.environ['DATABASE_URL']).username

def create_connect():
    
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    
    dbname = url.path[1:]
    
    password = url.password
    
    host = url.hostname
    
    port = url.port

    con = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
        )
            
    return con

