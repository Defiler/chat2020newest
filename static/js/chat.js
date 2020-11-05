username = "Guest"
REFRESH = 1000

window.addEventListener('load', function(){
    readChat();
})

function getMsg(){
    let msg = document.getElementById('message')
    let msgValue = msg.value // /nick Vards 
    msg.value = ''

    let komanda = msgValue.split(" ") // ['/nick', 'Vards']

    switch(komanda[0]){
        case "/nick": // nomainam username
            sendMsg(username + " changed nick to " + komanda[1])
            username = komanda[1]
            break;
        case "/joke": // genere Chuck Norris joku
            getChuckNorrisJoke()
            break;            
        default: // visi citi gadijumi (komanda nav atrasta)
            sendMsg(msgValue, username)

    }

}

function getMsgRow(msgText, msgUser){
    let msgHTML = "<li class='left clearfix'><div class='chat-body clearfix'><i>26.10. 8:30</i> <b>" + msgUser + ": </b>" + msgText + "</div></li>" 
    return msgHTML
}

async function sendMsg(msgText, msgUser = "Admin"){
    let data = JSON.stringify({"user":msgUser, "msg":msgText})

    let response = await fetch('/chat',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: data
    })

    readChat()
}

async function getChuckNorrisJoke(){
    let response = await fetch('https://api.chucknorris.io/jokes/random')
    let data_json = await response.json()
    sendMsg(data_json.value, "Chuck Norris")
}

async function readChat(){
    let response = await fetch('chat/get')
    let data_json = await response.json()
    
    let chats = document.getElementById('chats')
    chats.innerHTML = ''

    for(let message of data_json.chatMsg){
        msgHTML = getMsgRow(message.msg, message.user)
        chats.innerHTML = chats.innerHTML + msgHTML
    }

    await new Promise(resolve => setTimeout(resolve, REFRESH))
    await readChat()
}