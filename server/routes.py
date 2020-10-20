from server.app import app
from flask import send_file
from flask import Flask
from flask import request
from fetch.fetch_data import write
from publish.public import publish
import csv
from flask import Blueprint
import sys

api = Blueprint('api', __name__)


@api.route('/send-primary-data/<fetch_site>', methods=['POST'])
def get_data(fetch_site):
    try:
        data = request.get_data()
        f = open(sys.path[0] +
                 '/fetch/input/input_{}.csv'.format(fetch_site), 'wb')
        f.write(data)
        f.close()
        f = open(sys.path[0] +
                 '/fetch/output/output_{}.csv'.format(fetch_site), 'w')
        f.close()
        write(fetch_site)
        return send_file(sys.path[0] + '/fetch/output/output_{}.csv'.format(fetch_site),
                         mimetype='text/csv')
    except Exception as ex:
        return str(ex)


@api.route('/send-new-file/<fetch_site>', methods=['POST'])
def push_new_file(fetch_site):
    try:
        data = request.get_data()
        f = open(sys.path[0] +
                 '/fetch/output/output_{}.csv'.format(fetch_site), 'wb')
        f.write(data)
        return 'ok'
    except Exception as ex:
        return str(ex)


@api.route('/publish/<fetch_site>', methods=['POST'])
def publish_data(fetch_site):
    try:
        logs = publish(fetch_site)
        return 'logs: ' + logs
    except Exception as ex:
        return str(ex)
