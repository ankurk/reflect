function updateClock(){
    var now = moment()
    document.getElementById('time').innerHTML= now.format('h:mm');
    document.getElementById('date').innerHTML= now.format('dddd, MMM DD');
}
window.onload=function(){
    updateClock();
    setInterval(updateClock,60000);
}
