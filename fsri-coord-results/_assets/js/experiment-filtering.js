$(function() {
  var fire_location = '#fire-location=(.*)';
  var ventilation = '#ventilation=(.*)';

  $(window).on('hashchange', function() {
    if (window.location.hash) {
      var mat = window.location.hash.match(fire_location);
      var mat2 = window.location.hash.match(ventilation);

      if (mat || mat2) {
        if (mat) {
          $('.experiment-list li[data-fire-location]').show();
          $('.experiment-list li[data-fire-location][data-fire-location!=' + mat[1] + ']').hide();
        }
        if (mat2) {
          $('.experiment-list li[data-fire-location]').show();
          $('.experiment-list li[data-fire-location][data-ventilation!=' + mat2[1] + ']').hide();
        }
      }
      else {
        $('.experiment-list li[data-fire-location]').show();
      }
    }
  });

  $(window).trigger('hashchange');
});
