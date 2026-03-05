from flask import Flask
import redis
import os
import socket

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        redis_client.incr('hits')
        hits = redis_client.get('hits').decode()
        return f"""
        <h1>Hello, World!</h1>
        <p>From Flask + Redis Application</p>
        <p>Hostname: {socket.gethostname()}</p>
        <p>Visits: {hits}</p>
        """
    except:
        return f"""
        <h1>Hello, World!</h1>
        <p>From Flask Application (Redis unavailable)</p>
        <p>Hostname: {socket.gethostname()}</p>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
