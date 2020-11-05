from flask import Flask, render_template, request
import chats

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/getParam', methods = ['GET'])
def getParam():
    #print(request.args.get('vards'))
    return f"It Works! {request.args.get('vards')}"


@app.route('/postMsg', methods = ['POST'])
def postMsg():
    #print(request.json)
    data = request.json
    return f"This is post! {data['vards']}"

@app.route('/info', methods = ['GET', 'POST'])
def info():
    if request.method == 'GET':
        if request.args.get('vards'):
            return f"Hello, {request.args.get('vards')}!"
        else:
            return "Hello, stranger!"

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            dati = request.json
            return dati
        else:
            return f"Wrong content type: {request.content_type}"
    else:
        return "Unknow request method"


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