import sqlite3
db='car.db'
conn=sqlite3.connect(db)

conn.execute("DROP TABLE IF EXISTS makes")
# conn.execute("DROP TABLE IF EXISTS models")
# conn.execute("DROP TABLE IF EXISTS makes_models")


conn.execute("""CREATE TABLE IF NOT EXISTS makes
                (make_id INTEGER PRIMARY KEY,
                make_name VARCHAR,
                model_name VARCHAR,
                year VARCHAR,
                price INTEGER,
                zip VARCHAR,
                mrsp INTEGER);
                """)


conn.execute("""CREATE TABLE IF NOT EXISTS models
                (model_id INTEGER PRIMARY KEY,
                model_name VARCHAR);
                
                """)




conn.execute("""CREATE TABLE IF NOT EXISTS makes_models
                (make_id INTEGER,
                model_id INTEGER,
                FOREIGN KEY(make_id) REFERENCES makes(make_id),
                FOREIGN KEY(model_id) REFERENCES models(model_id));
                """)




conn.commit()
conn.close()