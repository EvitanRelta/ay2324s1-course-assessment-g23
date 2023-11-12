import psycopg2
import os
import traceback
from fastapi import HTTPException

def _get_env_variable(key: str) -> str:
    value = os.getenv(key)
    assert value is not None, f'Environment variable "{key}" not found.'
    return value

def connect():
    try:
        conn = psycopg2.connect(
            host=_get_env_variable("POSTGRES_HOST"),
            port=_get_env_variable("POSTGRES_PORT"),
            database=_get_env_variable("POSTGRES_DB"),
            user=_get_env_variable("POSTGRES_USER"),
            password= _get_env_variable("POSTGRES_PASSWORD"))
        return conn
    except Exception:
        traceback.print_exc()

def execute_sql_write(sql_command: str, params: tuple=None):
    conn = connect()
    try:
        with conn, conn.cursor() as cur:
            if params:
                cur.execute(sql_command, params)
            else:
                cur.execute(sql_command)

            conn.commit()

    except psycopg2.DatabaseError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

def execute_sql_read_fetchone(sql_command: str, params: tuple=None):
    conn = connect()
    try:
        with conn, conn.cursor() as cur:
            if params:
                cur.execute(sql_command, params)
            else:
                cur.execute(sql_command)
            return cur.fetchone()

    except psycopg2.DatabaseError as e:
        raise HTTPException(status_code=500, detail="Internal server error1")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error2")

def execute_sql_read_fetchall(sql_command: str, params: tuple=None):
    conn = connect()
    try:
        with conn, conn.cursor() as cur:
            if params:
                cur.execute(sql_command, params)
            else:
                cur.execute(sql_command)
            return cur.fetchall()

    except psycopg2.DatabaseError as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")