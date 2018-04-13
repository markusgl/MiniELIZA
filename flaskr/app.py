from flask import Flask, request
from flask.sessions import SecureCookieSessionInterface
import json
import eliza_core as ec
from flaskr.message import Message, MessageSchema
from marshmallow import ValidationError
import logging

logging.basicConfig(filename='error.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ask", methods=['POST'])
def send_message():
    """
    request_data = json.dumps(request.get_json())
    try:
        message_schema = MessageSchema()
        message, errors = message_schema.load(request_data)

    except ValidationError as err:
        logger.error("JSON Validation failed: %s" % err)
    """

    response = ec.send_message(request.get_json()["message"])

    return response


if __name__ == '__main__':
    app.session_interface = SecureCookieSessionInterface()
    app.run()
