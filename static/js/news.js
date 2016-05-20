function updateNews(){

    $.getJSON($SCRIPT_ROOT + '/_get_news_headlines', function(data) {
        console.log('Retrieved news headlines');
        $("#headlines").empty();
        var headlines = data.content;
        var numHeadlines = headlines.length;
        for(var i=0; i < numHeadlines; i++) {
            $("#headlines").append("<tr><td><i class='material-icons'>library_books</i>&emsp;" + headlines[i] + "</td></tr>");
        }
    });
    return false;
}

$( document ).ready( function() {
    updateNews();
    setInterval(updateNews,1200000);
});