from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_counts():
    conn = psycopg2.connect(
        host="db",
        database="votes",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT vote, COUNT(*) FROM votes GROUP BY vote")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

@app.route('/')
def index():
    counts = get_counts()
    return render_template('index.html', counts=counts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
