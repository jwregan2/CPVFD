$(function() {
  var pages = 1;
  var itemsPerPage = 5;
  var itemsFilteredTotal;
  var filterType = 'all';

  var images = assets.images.filter(function(image) {
    for (var i = 0; i < multimedia.images.length; i++) {
      if (image.startsWith(window.baseurl + assetPath + multimedia.images[i])) {
        return true;
      }
    }
  });

  images = images.map(function(image) {
    // Strip off hash for thumbnails since we don't know the generated hashes when thumbs are generated
    var stripped = image.replace(/-[a-f0-9]+\.(.*)$/, '.$1').replace(/\/assets/g, '/assets/thumbnails');
    return {
      href: image,
      thumbnail: stripped
    };
  });

  function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
  }

  shuffle(images);

  var filter = function() {
    return shouldDisplay(filterType, $(this));
  };

  function addBig(ths) {
    $(ths).addClass('big');
  }

  function removeBig(ths) {
    $(ths).removeClass('big');
  }

  var templates = {};
  _.each($("script[type='text/template']"), function(e) {
    templates[$(e).attr('id')] = _.template($(e).html());
  });

  _.each(images, function(e, idx) {
    var $el = $(templates.gridItem({i: e, idx: idx}));
    e.el = $el;
    e.idx = idx;
    $('.isotope-container').append($el);
  });

  function shouldDisplay(category, $el) {
    var filtered = category === 'all' ? images : images.filter(function(image) { return (image.type === category); });
    itemsFilteredTotal = filtered.length;
    var all = filtered.slice(0, (pages * itemsPerPage));
    var curidx = $el.data('idx');
    _.each(images, function(e) {
      removeBig(e.el);
    });

    // Set big tiles.
    var bigTileCount = 0;
    var betweenBigTileCount = 0;
    var smallTileRowsBetweenBigTiles = 2;
    var tilesBetween;
    _.forEach(all, function(e) {
      if (bigTileCount % 2 === 0) {
        // Left big tile.
        tilesBetween = 2 + smallTileRowsBetweenBigTiles * 4;
        if (betweenBigTileCount === tilesBetween || bigTileCount === 0) {
          addBig(e.el);
          bigTileCount++;
          betweenBigTileCount = 0;
        } else {
          betweenBigTileCount++;
        }
      } else {
        // Right big tile.
        tilesBetween = 6 + smallTileRowsBetweenBigTiles * 4;
        if (betweenBigTileCount === tilesBetween) {
          addBig(e.el);
          bigTileCount++;
          betweenBigTileCount = 0;
        } else {
          betweenBigTileCount++;
        }
      }
    });

    return all.map(function(a) { return a.idx; }).includes(curidx);
  }

  var iso = $('.multimedia .isotope-container').isotope({
    itemSelector: '.multimedia .item',
    percentPosition: true,
    initLayout: false,
    masonry: {
      columnWidth: '.multimedia .sizer'
    },
    filter: filter
  });

  iso.on('layoutComplete', function() {
    $('.multimedia .grid-container').addClass('-show');
    window.setTimeout(function() {
      var ht = $('.multimedia .isotope-container').height();
      $('.multimedia .grid-container').height(ht);
    }, 0);
  });

  iso.isotope();

  function hideLoadMoreIfAllDisplayed() {
    $('.load-more').css('display', ((pages * itemsPerPage) >= itemsFilteredTotal) ? 'none' : 'block');
  }

  $('.load-more').click(function() {
    pages++;
    ga('send', 'event', 'multimedia-load-more', 'clicked');

    hideLoadMoreIfAllDisplayed();

    iso.isotope({
      filter: filter
    });
  });
});
