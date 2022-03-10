from flask import Flask, request, jsonify
import requests
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
import logging


logging.basicConfig(level=logging.INFO)
logging.info("Setting LogLevel to INFO")

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)
db = SQLAlchemy(app)
metrics = PrometheusMetrics(app)

metrics.info("api", "Up and running", version="1.0")

@app.route("/helloworld")
@cache.cached(timeout=30, query_string=True)
def get_helloworld(): 
    return jsonify({"msg": "Hello World"})

@app.route("/status")
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def status_check():
    return jsonify({"status": "Up"})
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    
