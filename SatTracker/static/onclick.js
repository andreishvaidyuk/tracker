var start = document.querySelector('.start'),
    stop = document.querySelector('.stop'),
    websocket = new WebSocket('ws://127.0.0.1:5000/');
start.onclick = function(event){
    websocket.send(JSON.stringify({action: 'start'}));
    }
stop.onclick = function(event){
    websocket.send(JSON.stringify({action: 'stop'}));
    }
websocket.onmessage = function(event){
    data = JSON.parse(event.data);
    }