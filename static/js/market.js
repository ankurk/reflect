function updateMarket(){

    $.getJSON($SCRIPT_ROOT + '/_get_market_prices', function(data) {
        console.log('Retrieved market data');
        $("#market").empty();
        var content = data.content;
        var stocks = content.stocks;
        var currs = content.currencies;
        var html = "<tr><td>"

        for(var i=0; i < stocks.length; i++) {
            var changeId = 'change' + i;
            html = html + stocks[i].symbol + "&nbsp;&nbsp;" + stocks[i].price + "&nbsp;&nbsp;<span id='" + changeId + "'>" + stocks[i].change_percent + "%</span>&emsp;";
        }
        for(var i=0; i < currs.length; i++) {
            html = html + currs[i].symbol + "&nbsp;&nbsp;" + currs[i].price +  "&emsp;";
        }
        html = html + "</td></tr>";
        $("#market").append(html);
        for(var i=0; i < stocks.length; i++) {
            if (stocks[i].change_percent > 0) {
                $('#change'+i).addClass('upChange');
            } else if (stocks[i].change_percent < 0) {
                $('#change'+i).addClass('downChange');
            }
        }
    });
    return false;
}

$( document ).ready( function() {
    updateMarket();
    setInterval(updateMarket,300000);
});