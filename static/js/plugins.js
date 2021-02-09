$(document).ready(function(){
    
    $objWindow = $(window);
    
    //Parallax
    $('.bg_parallax').each(function(){
        var $bgObj = $(this);
        $(window).scroll(function(){
            var speed = 3;
            var yPos = -($objWindow.scrollTop()/speed);
            var coords = '100% '+ yPos + 'px';
            $bgObj.css({ backgroundPosition: coords});
        });
    });
    
    
    //Grid masonry
    $('.grid').masonry({
            itemSelector: '.grid-item',
            stamp: '.stamp',
      });
    
   $('#home').click(function(){
       $('html, body').animate({scrollTop:0}, 500);  
            return false;
        });
    
    $('.main-menu li a').click(function(){
        var id = $(this).attr('id');
        $('html, body').animate({
            scrollTop: $('.' + id).offset().top-70}, 500);
            return false;
        });
    
});