from flask import Flask, request, redirect
import twilio.twiml
import os
import urllib
import string
import random
from pb_py import main as api

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+19799857131": "Audi",
    "+19799857132": "Atif",
    "+19799857169": "Alok",
}

@app.route("/", methods=['GET', 'POST'])
def communicator():
    """Respond and greet the caller by name."""

    # Retrieved information from SMS Twilio
    from_number = request.values.get('From', None)
    message_body = request.values.get('Body', "")
    date_created = request.values.get('DateCreated', "")
    account_sid = request.values.get('AccountSid', "")
    date_created = request.values.get('DateCreated', "")


    if from_number in callers:
        message = callers[from_number] + ", thanks for the message:" + message_body + "!"
    else:
        message = "Buddy, thanks for the message!" + message_body


    #bot_response = talk(message_body)
    # bot_response = api.talk('2a2a1569fe48655c89487a7e8c6cb214', '1409612442334', 'http://aiaas.pandorabots.com', 'alok', message_body)["response"]

    resp = twilio.twiml.Response()
    resp.message(bot_response)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
