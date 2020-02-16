import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']
conn = redis.Redis(host='redis', port=6379)
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()