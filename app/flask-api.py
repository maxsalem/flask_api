from flask import Flask, request
import json

app = Flask(__name__)

description =   """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>
                    <h3>A simple API using Flask</h3>
                    <a href="http://localhost:5000/api?value=10">sample request</a>
                </body>
                """

@app.route('/', methods=['GET'])
def hello_world():
    return description

@app.route('/api', methods=['GET'])
def square():
    if not all(k in request.args for k in (["value"])):
        error_message = f"\
                        Required parameters : 'value'<br>\
                        Supplied parameters : {[k for k in request.args]}\
        "
        return error_message
    else:
        value = request.args.get('value', type=int)
        return json.dumps({"Value Squared": value**2})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)