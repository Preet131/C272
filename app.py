import os

from flask import Flask, request, jsonify, render_template, redirect, url_for,send_file
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from werkzeug.utils import secure_filename

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

# Add your Twilio credentials
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'ACdf38aa1c9bc39c5c1c90e1d6e9c87372'
    TWILIO_SYNC_SERVICE_SID = 'IS9273be50834bfe6e9240a0958ebfebd7'
    TWILIO_API_KEY = 'SK38add3221b5ab1379116191cdaeb52dd'
    TWILIO_API_SECRET = 'NNI2qqenOVgxsGRN4971JvfIHJkW2D3I'

    username = request.args.get('username', fake.user_name())

    # create anccess toke with credentials
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    # create a Sync grant and add to token
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    textFromNotepad = request.form['text']
    with open('workfile.txt', 'w') as f:
        f.write(textFromNotepad)
    pathToStoreTxt = "workfile.txt"
    return send_file(pathToStoreTxt, as_attachment=True)



if __name__ == "__main__":
    app.run(host= 'localhost', port=5001, debug=True)

    
        

    

    


if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
