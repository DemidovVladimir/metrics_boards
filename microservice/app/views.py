import requests
from flask import render_template, request
from app import app, metrics
from prometheus_flask_exporter import PrometheusMetrics
from requests.exceptions import Timeout
import os

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

@app.route('/versions')
def versions():
    headers = {
        "PRIVATE-TOKEN": os.getenv('GITLAB_TOKEN')
    }
    repo_name = None
    try:
        response = requests.get("https://gitlab.com/api/v4/users/"+os.getenv('REPO_ID')+"/projects", headers=headers)
        repo_name = response.json()[0].get('name')
        metrics.info('Dependency_angular', 'Should be replaced with version...', version=repo_name)
    except Timeout:
        print('The request timed out')
    except Error as err:
        print(err)
    else:
        print('The request did not time out')
    return repo_name, 200

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)
