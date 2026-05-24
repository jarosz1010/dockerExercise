import time
import redis
from flask import Flask

app = Flask(__name__)
# Połączenie z Redisem – nazwa hosta 'redis' odnosi się do nazwy usługi w Docker Compose
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'<h1>Cześć! Ta strona była odwiedzona {count} razy.</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)