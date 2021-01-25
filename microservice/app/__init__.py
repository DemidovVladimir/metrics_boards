import os
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask
app = Flask(__name__)

metrics = PrometheusMetrics(app, group_by='endpoint')
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

from app import views

if __name__ == 'app':
    app.run(debug=False,host='0.0.0.0', port=os.getenv('PORT'))