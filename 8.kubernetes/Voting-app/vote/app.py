from flask import Flask, render_template, request
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form['vote']
        redis_client.rpush('votes', vote)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
