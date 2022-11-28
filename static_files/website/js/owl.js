$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    margin: 3,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 4,
      },
      1000: {
        items: 6,
      },
    },
  });
});