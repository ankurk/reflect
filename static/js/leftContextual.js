function updateDirections(data) {
    $("#leftContextual").empty();
    $("#leftContextual").append("<tr><td><span id='travelTime'>"+data.traffic_time+"</span> to work via "+data.route+"</td></tr>");

    // update style according to traffic
    var with_traffic = data.traffic_time.replace(/[^0-9]/g,'');
    var no_traffic = data.normal_time.replace(/[^0-9]/g,'');
    if (with_traffic > (no_traffic*1.3)) {
        $('#travelTime').addClass('redTravelTime');
    } else if (with_traffic > (no_traffic*1.1)) {
        $('#travelTime').addClass('orangeTravelTime');
    } else {
        $('#travelTime').addClass('greenTravelTime');
    }
}


function updateContextual(){

    $.getJSON($SCRIPT_ROOT + '/_get_contextual', function(data) {

        if (data.type == 'direction') {
            updateDirections(data);
        }
      });
      return false;
}

$( document ).ready( function() {
    updateContextual();
    setInterval(updateContextual,1200000);
});