from flask import render_template
from app import app, metrics
from prometheus_flask_exporter import PrometheusMetrics

@app.route('/')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'status': lambda resp: resp.status_code
    })
def home():
   return "BMW rules!"

@app.route('/template')
def template():
    return render_template('home.html')
