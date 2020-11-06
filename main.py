from flask import Flask, render_template, request
import chats

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods = ['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            dati = request.json
            chats.write(dati)
            return "JSON OK"
    else:
        return f"This request method {request.method} is not allowed!"


@app.route('/chat/get')
def getChat():
    return chats.read()

app.run(host='0.0.0.0', port=80, debug=True)