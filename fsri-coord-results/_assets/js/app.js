$(function() {

  window.trackTrainingLaunch = function(elem) {
    ga('send', 'event', 'launchTraining', elem.name);
  };

  $.fancybox.defaults.loop = true;
  tippy('[title]');

  imageMapResize();

  $('.table-hover').on('click', 'tr', function() {
      var $a = $(this).find('a').last();
      if ($a.length) {
          window.open($a.attr('href'), $a.attr("target") || '_self');
      }
  });

  $(".newsletter__right__button").click(function(evt) {
    evt.preventDefault();
    ga('send', 'event', 'popup', 'newsletter');
    vex.open({
      unsafeContent: '<div class="newsletter__popup page-home__resources__right__title">Mailing List</div><div class="page-home__resources__right__separator"></div><form id="mktoForm_6453"></form>',
      afterOpen: function() {
        MktoForms2.loadForm("//app-ab11.marketo.com", "365-LEA-623", 6453);
      }
    });
  });

  $('#nav-toggle').click(function() {
    $(this).toggleClass('active');
    $('#nav-overlay').toggleClass('open');
  });

  $('.page-home__research__left__container').slick({
    vertical: true,
    verticalSwiping: true,
    slidesToShow: 3,
    prevArrow: '<button type="button" class="slick-prev vertical">Previous</button>',
    nextArrow: '<button type="button" class="slick-next vertical">Next</button>'
  });

  function regExpUrl() {
    return new RegExp('(https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9]\\.[^\\s]{2,})', 'g');
  }

  function sanitize(input) {
    return input.replace(/<script[^>]*?>.*?<\/script>/gi, '')
      .replace(/<[\/\!]*?[^<>]*?>/gi, '')
      .replace(/<style[^>]*?>.*?<\/style>/gi, '')
      .replace(/<![\s\S]*?--[ \t\n\r]*>/gi, '');
  }

  $('a[data-more]').click(function() {
    $('.more').toggleClass('show');
    $(this).hide();
  });

  var bio = _.template($("#bio_popup").html());
  $(document).on('click', 'a.person', function(evt) {
    evt.preventDefault();
    var person = $(this).data('person');
    ga('send', 'event', 'popup', 'bio', person);
    vex.open({
      unsafeContent: bio({i: people[person] })
    });
  });

  var _event = _.template($("#event").html());
  $(document).on('click', '.event-trigger', function(evt) {
    evt.preventDefault();
    var idx = $(this).data('event');

    ga('send', 'event', 'popup', 'event', events[idx].title);

    vex.open({
      unsafeContent: _event({i: events[idx], idx: idx})
    });
  });

  //
  // Detail
  //

  $('.detail__body__content__images').css('display', 'block');
  $('.detail__body__content__images__carousel').on('init', function() {
    // Prevent fancybox from showing duplicate images that are created by slick's infinite looping.
    // We can accomplish this by removing the 'data-fancybox' attribute from duplicated elements.
    var elements = $('.detail__body__content__images__carousel__element');
    var uniqueElements = _.uniqWith(elements, function(a, b) {
      var $imageA = $(a).find('.detail__body__content__images__carousel__element__content');
      var $imageB = $(b).find('.detail__body__content__images__carousel__element__content');
      return ($imageA.attr('href') === $imageB.attr('href'));
    });

    _.each(elements, function(element) {
      // Use slick's indices to determine if this was an original or a duplicate.
      var slickIndex = element.dataset.slickIndex;
      if (slickIndex < 0 || slickIndex >= uniqueElements.length) {
        var $image = $(element).find('.detail__body__content__images__carousel__element__content');
        $image.removeAttr('data-fancybox');
      }
    });
  });
  $('.detail__body__content__images__carousel').slick({
    slidesToShow: 1,
    autoplay: false,
    arrows: true,
    dots: true
  });

  $('.detail__body__content__videos').css('display', 'block');
  $('.detail__body__content__videos__carousel').slick({
    slidesToShow: 1,
    autoplay: false,
    arrows: true,
    dots: true
  });

  $('.detail__body__content__more').css('display', 'block');
  $('.detail__body__content__more__carousel').slick({
    slidesToShow: 1,
    autoplay: false,
    arrows: true,
    dots: true
  });

  $('.detail__body__content__partners').css('display', 'block');
  $('.detail__body__content__partners__carousel').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: false,
    arrows: true,
    dots: true
  });

  //
  // Project List
  //

  $('.project-list__body__right__bloc__events .events').slick({
    vertical: true,
    verticalSwiping: true,
    slidesToShow: 3,
    infinite: false,
    prevArrow: '<button type="button" class="slick-prev vertical">Previous</button>',
    nextArrow: '<button type="button" class="slick-next vertical">Next</button>'
  });

  //
  // Members / Logout
  //

  var memberPath = Cookies.get('MemberPath') || '';

  if (memberPath) {
    $(".members-link").attr('href', memberPath + 'index.html');
  }

  $(".navbar__links__link.logout-link").css('display', (memberPath) ? 'inline-block' : 'none');
  $(".navbar__burger-links__link.logout-link").css('display', (memberPath) ? 'block' : 'none');

  $(".logout-link").click(function(e) {
    e.preventDefault();

    $.ajax({
      url: logoutApiUrl + '?memberPath=' + encodeURIComponent(memberPath),
      method: 'GET',
      xhrFields: {
        withCredentials: true
      }
    }).done(function(data, status, xhr) {
      window.location.reload();
    });

    return false;
  });

  //
  // Experiment
  // TODO: Put this in 'experiment.js'. For some reason custom_js is not working in 'experiment.html'...
  //
  $('.floorplan .sensor').fancybox({
    type: 'iframe',
    iframe: {
      css: {
        width: '100%',
        height: '100%'
      }
    },
    buttons: [
      'fullScreen',
      'close'
    ]
  });

  $('.floorplan .panorama').fancybox({
    type: 'iframe',
    iframe: {
      css: {
        width: '100%',
        height: '100%'
      }
    },
    buttons: [
      'fullScreen',
      'close'
    ]
  });

  $('.etr-table .circuit').fancybox({
    type: 'iframe',
    iframe: {
      css: {
        width: '100%',
        height: '100%'
      }
    },
    buttons: [
      'fullScreen',
      'close'
    ]
  });

  // Layer buttons.
  var showPanoramas = true;
  $('.section.layers .button.panoramas').click(function(ev) {
    $(ev.target).toggleClass('active');
    showPanoramas = !showPanoramas;
    var $panoramas = $('.floorplan .panorama');
    $panoramas.css('pointer-events', (showPanoramas) ? 'auto' : 'none');
    $panoramas.css('opacity', (showPanoramas) ? '1' : '0');
  });

  var showSensors = true;
  $('.section.layers .button.sensors').click(function(ev) {
    $(ev.target).toggleClass('active');
    showSensors = !showSensors;
    var $sensors = $('.floorplan .sensor');
    $sensors.css('pointer-events', (showSensors) ? 'auto' : 'none');
    $sensors.css('opacity', (showSensors) ? '1' : '0');
  });

  // Floor buttons.
  var currentFloor = '1';
  $('.section.floors .button').click(function(ev) {
    var selectedFloor = $(ev.target).data('floor');
    if (selectedFloor === currentFloor) {
      return;
    }

    $('.section.floors .button[data-floor="' + currentFloor + '"]').removeClass('active');
    $('.section.floors .button[data-floor="' + selectedFloor + '"]').addClass('active');

    currentFloor = selectedFloor;

    // Show the selected floor and hide the others.
    _.forEach($('.floorplan'), function(floorplan) {
      var $floorplan = $(floorplan);
      if ($floorplan.data('floor') === currentFloor) {
        $floorplan.show();
      } else {
        $floorplan.hide();
      }
    });
  });
});


//
// Comparison: Back to Top Button
//
var toggleHeight = $(window).outerHeight() * 2;

$(window).scroll(function() {
	if ($(window).scrollTop() > toggleHeight) {
		$(".backtotop").addClass("active");
	} else {
		$(".backtotop").removeClass("active");
	}
});

//Scrolls the user to the top of the page
$(".backtotop").click(function() {
	$("html, body").animate({ scrollTop: 0 }, "slow");
	return false;
});
