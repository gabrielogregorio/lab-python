from flask import *

app = Flask(__name__)

@app.route('/')
def principa():
    return jsonify({'version': 0.1})

app.run(port=1022, host='127.0.0.1')
