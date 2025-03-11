from flask import Flask
import json
import logging
app = Flask(__name__)

def log(endPoint, message):
    app.logger.info(str(endPoint) + " called with this result: " + str(message))

@app.route("/")
def hello():
    log("/(root)", "successfull")
    #app.logger.info("/ called with this result: successfull")
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    log("/status", response.response)
   #app.logger.info("/status called with this result: " + str(response))

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    log("/metrics", response)
    #app.logger.info("/metrics called with this result: " + response)
    return response

if __name__ == "__main__":
     # Stream logs to a file, and set the default log level to DEBUG
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')

