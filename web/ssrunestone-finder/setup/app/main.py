from flask import Flask, request, render_template, redirect
from flask_assets import Environment, Bundle
from rq import Queue
from rq.job import Job
from subprocess import check_output

import redis, re, time, uuid, string, socket

app = Flask(__name__)
assets = Environment(app)
scss = Bundle('jobs.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)
redis_ip = socket.gethostbyname('redis')
conn = redis.Redis(host='redis', port=6379)
q = Queue(connection=conn)

def _is_safe(url):
    """
    Unhackable SSRF security!
    """
    ssrf_security = [
        lambda url: url.startswith("http") or url.startswith("gopher"),
        lambda url: all([val not in url for val in ["127.0.0.1", "redis", "localhost", "0.0.0.0", redis_ip]])
    ]
    return all([d(url) for d in ssrf_security])

def _get_jobs_from_registry(registry):
    job_ids = registry.get_job_ids()
    return Job.fetch_many(job_ids, connection=conn)

def _get_all_jobs():
    registries = [
        q.finished_job_registry,
        q.started_job_registry,
        q.failed_job_registry,
        q.scheduled_job_registry
    ]
    jobs = []
    for reg in registries:
        jobs += _get_jobs_from_registry(reg)
    return jobs

def _is_missing(param):
    return param is None or param == ''

def _get_form_params(*params):
    values = [request.form.get(p) for p in params]
    return values

def count_dollars(url):
    """
    Count runestones
    """
    if not _is_safe(url):
        return 0, 0, None
    response = ''.join([chr(x) for x in check_output(["curl", "-L", url], timeout=5) if chr(x) in string.printable])
    words = len(response.split(" "))
    dollars = len([c for c in response.split(" ") if c == "runestone"])
    return words, dollars, response


@app.route("/jobs/submit", methods=["POST"])
def submit():
    params = _get_form_params("name", "url")
    if any([_is_missing(p) for p in params]):
        return "Parameters missing..."
    name, url = params

    job = Job.create(
        count_dollars,
        (url,),
        meta={"name": name, "tag": "tag"+str(uuid.uuid4()).replace('-','')},
        connection=conn,
        ttl=500,
        failure_ttl=500
    )
    q.enqueue_job(job)
    time.sleep(1)

    return redirect("/jobs", code=302)

@app.route("/")
@app.route("/jobs")
def jobs():
    jobs = _get_all_jobs()
    return render_template('jobs.html', jobs=jobs, redis_ip=redis_ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)