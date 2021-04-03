from flask import send_file
from flask import Flask
from flask import request
from fetch.fetch_data import write
from publish.public import publish
import csv
from flask import Blueprint
import sys
from config import log

api = Blueprint('api', __name__)


@api.route('/send-primary-data/<fetch_site>', methods=['POST'])
def get_data(fetch_site):
    log.info('Start send primary data for ' + fetch_site)
    try:
        data = request.get_data()
        f = open(sys.path[0] +
                 '/fetch/input/input_{}.csv'.format(fetch_site), 'wb')
        f.write(data)
        f.close()
        f = open(sys.path[0] +
                 '/fetch/output/output_{}.csv'.format(fetch_site), 'w')
        f.close()
        log.info('Input data write success')
        write(fetch_site)
        return send_file(sys.path[0] + '/fetch/output/output_{}.csv'.format(fetch_site),
                         mimetype='text/csv')
    except Exception as ex:
        return str(ex)


@api.route('/send-new-file/', methods=['POST'])
def push_new_file():
    log.info('Start send result file')
    try:
        data = request.get_data()
        f = open(sys.path[0] +
                 '/fetch/output/output.csv', 'wb')
        f.write(data)
        return 'Success'
    except Exception as ex:
        log.error(str(ex))
        return str(ex)


@api.route('/publish/', methods=['POST'])
def publish_data():
    log.info('Start publish content')
    try:
        logs = publish()
        print(logs)
        log.info('Answer from server: ' + str(logs))
        return 'logs: ' + logs
    except Exception as ex:
        log.error(str(ex))
        return str(ex)
