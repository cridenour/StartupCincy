$(function() {
  var slider = setInterval(function() {
    $('.slider .slides .active').fadeOut(function() {
      $(this).removeClass('active').appendTo('.slider .slides');
    }).next().fadeIn(function() {
        $(this).addClass('active');
      });

    if($('.slider-controls li.active').next().length == 0) {
      $('.slider-controls li.active').removeClass('active');
      $('.slider-controls li:first-child').addClass('active');
    } else {
      $('.slider-controls li.active').removeClass('active').next().addClass('active');
    }
  }, 5000);

  $('.slider-controls li a').click(function(e) {
    $('.slider .slides .active').fadeOut();
    clearInterval(slider);
    $('#' + $(this).attr('data-for')).fadeIn().addClass('active');
    $('.slider-controls li.active').removeClass('active');
    $(this).parent().addClass('active');
    e.preventDefault();
  });
});



















