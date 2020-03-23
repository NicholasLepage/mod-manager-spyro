import sqlite3 as lite


def initiate_db():
    conn = lite.connect("info.db")

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE spyro_location(
        path text
    )
    """)

    cur.execute("""
    CREATE TABLE mods_location(
        path text,
        enabled integer
    )
    """)

    conn.commit()

    conn.close()
