$(document).ready(function(){
    $objWindow = $(window);
    $('.bg_parallax').each(function(){
        var $bgObj = $(this);
        $(window).scroll(function(){
            var speed = 5;
            var yPos = -($objWindow.scrollTop()/speed);
            var coords = '100% '+ yPos + 'px';
            $bgObj.css({ backgroundPosition: coords});
        });
    });
});
