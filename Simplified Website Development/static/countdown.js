setInterval(function time() {
    var d = new Date();
    var hours = 24 - d.getHours();
    var min = 60 - d.getMinutes();
    if ((min + '').length == 1) {
        min = '0' + min;
    }
    var sec = 60 - d.getSeconds();
    if ((sec + '').length == 1) {
        sec = '0' + sec;
    }

    jQuery('#the-final-countdown p').html(hours + ':' + min + ':' + sec);

    if (hours == 0 && min == 0 && sec == 0) {
        $.ajax({
            url: '/countdown_reached',
            method: 'POST',
        });
    }
}, 1000);