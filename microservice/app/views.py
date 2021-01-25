from flask import render_template, request
from app import app, metrics
from prometheus_flask_exporter import PrometheusMetrics

common_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

@app.route('/')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'status': lambda resp: resp.status_code
    })
@common_counter
def home():
    app.logger.info(type(metrics))
    return "BMW rules!"

@app.route('/template')
def template():
    return render_template('home.html')

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)
