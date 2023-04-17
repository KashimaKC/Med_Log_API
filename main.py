from flask import *

import json, time
# run this python file to start the API

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = [{'message': 'success', 'date': '2023-01-01', 'painRating': 4, 'notes': 'sample', 'id': 1},
                {'message': 'success', 'date': '2023-01-02', 'painRating': 4, 'notes': 'sample', 'id': 2}]
    resp_json = json.dumps(data_set)

    return resp_json

# /post/?one=INSERT_HERE
@app.route('/post/', methods=['GET'])
def post_request():
    date = str(request.args.get('date')) 
    pain = str(request.args.get('pain'))
    notes = str(request.args.get('notes'))

    # /post/?date=a1&pain=a2&notes=a3
    data = {'message': 'received post request', 'date': f'{date}', 'painRating': f'{pain}', 'notes': f'{notes}', 'time': time.time()}
    resp_json = json.dumps(data)

    return resp_json

if __name__ == '__main__':
    app.run(host="0.0.0.0")
