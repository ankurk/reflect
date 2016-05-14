function socketConnect(){
    var socket = io.connect('http://' + document.domain + ':' + location.port, {
        'reconnection' : true
    });

    socket.on('weather update', function(msg) {
        console.log('received weather update')
        //$('#log').append('<p>Received: ' + msg.data + '</p>');
    });

    socket.on('traffic update', function(msg) {
        console.log('received traffic update')
        //$('#log').append('<p>Received: ' + msg.data + '</p>');
    });

    socket.on('connect', function(msg) {
        console.log('Connected to server')
    });

    socket.on('reconnect_attempt', function(msg) {
        console.log('Reconnect attempted')
    });

    socket.on('connect_error', function(msg) {
        console.log('Connection Error')
    });
    socket.on('reconnect_error', function(msg) {
        console.log('reconnect_failed')
    });
//    $('form#emit').submit(function(event) {
//        socket.emit('my event', {data: $('#emit_data').val()});
//        return false;
//    });
//    $('form#broadcast').submit(function(event) {
//        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
//        return false;
//    });
}

window.onload=function(){
    socketConnect();
}