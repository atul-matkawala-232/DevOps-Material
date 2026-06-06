import time
import redis
import psycopg2
from psycopg2 import OperationalError

redis_client = redis.Redis(host='redis', port=6379)

def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="votes",
                user="postgres",
                password="postgres"
            )
            print("Connected to DB")
            return conn
        except OperationalError:
            print("DB not ready, retrying in 2 seconds...")
            time.sleep(2)

while True:
    vote = redis_client.lpop('votes')
    if vote:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote.decode(),))
        conn.commit()
        cur.close()
        conn.close()
        print("Inserted vote:", vote.decode())
    time.sleep(1)
