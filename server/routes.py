from server.app import app
from flask import send_file
from flask import Flask
from flask import request
from fetch.hamiltonwatch import write_hamiltonwatch
from publish.public import publish
import csv
from flask import Blueprint
import sys

api = Blueprint('api', __name__)


@api.route('/send-primary-data/<fetch_site>', methods=['POST'])
def get_data(fetch_site):
    # try:
    data = request.get_data()
    f = open(sys.path[0] + '/fetch/input/{}.csv'.format(fetch_site), 'wb')
    f.write(data)
    f.close()
    write_hamiltonwatch()
    return send_file(sys.path[0] + '/fetch/output/output_{}.csv'.format(fetch_site),
                     mimetype='text/csv')
    # except:
    #     return 'invalid data'


@api.route('/publish/<fetch_site>', methods=['POST'])
def push_to_site(fetch_site):
    try:
        logs = publish(fetch_site)
        open(
            sys.path[0] + '/fetch/output/output_{}.csv'.format(fetch_site), "w").close()
        return 'logs ' + logs
    except:
        return 'invalid data'
