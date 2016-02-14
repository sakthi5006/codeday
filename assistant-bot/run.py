from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+19799857131": "Audi",
    "+19799857132": "Atif",
    "+19799857169": "Alok",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    message_body = request.values.get('Message', "")

    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Buddy, thanks for the message!" + message_body

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
