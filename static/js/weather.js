function updateWeather(){

    $.getJSON($SCRIPT_ROOT + '/_get_weather', function(data) {
        $("#temp").html(data.currTemp + "&deg;");
        $("#minMax").html(data.maxTemp + "&deg;&emsp;" + data.minTemp  + "&deg;");
        $("#summ").text(data.summary);
        $("#rainProb").text(data.rainProb + "%");
        $("#sunrise").html("&#8613; " + data.sunrise);
        $("#sunset").html("&#8615; " + data.sunset);

        var day1 = data.forecasts[0]
        $("#day1DayOfWeek").text(day1[3]);
        $("#day1MinMax").html(day1[2] + "&deg;&emsp;" + day1[1]  + "&deg;");

        var day2 = data.forecasts[1]
        $("#day2DayOfWeek").text(day2[3]);
        $("#day2MinMax").html(day2[2] + "&deg;&emsp;" + day2[1] + "&deg;");

        var skycons = new Skycons({
             "monochrome" : false,
             "colors": {
                "cloud" : "#ABB7B7",
                "moon"  : "#6C7A89",
                "main"  : "#ECECEC",
                "sun"   : "#F7CA18"              }
             });
        skycons.add("currIcon", data.currIcon);
        skycons.add("day1Icon", day1[0]);
        skycons.add("day2Icon", day2[0]);
        skycons.add("rainIcon", Skycons.SLEET);
        skycons.play();
      });
      return false;
}

$( document ).ready( function() {
    updateWeather();
    setInterval(updateWeather,1200000);
});