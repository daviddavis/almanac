$().ready(function() {

    var release = new Date(2014, 2, 18);
    if(release > (new Date())) {
        countdown(function(ts) {
            $(".countdown").text(ts.toString());
        }, release);
    } else {
        $(".cd-container").text("Available in Stores Now!");
    }

    $('.fancybox').fancybox({helpers: {media: {}}});

});
