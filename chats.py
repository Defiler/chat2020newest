from flask import json, jsonify

CHAT_FILE = 'chats.txt'

def write(jsonData):
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(jsonData) + '\n')
    
def read():
    chatLines = []
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        for row in f:
            chatLines.append(json.loads(row))
    
    return jsonify({"chatMsg":chatLines})