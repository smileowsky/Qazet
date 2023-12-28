jQuery(document).ready(function($) {
    "use strict";

    /* Search */
    $(".search-trigger").on('click', function() {
        $(".search").slideToggle("slow", function() {});
	   $("i").toggleClass( "fa-times" , "fa-search");
    });

    // Prettyphoto
    $("a[class^='prettyPhoto']").prettyPhoto({
        theme: 'pp_default'
    });

    /* NewsTicker */
    $('#news-ticker').slick({
        dots: false,
        arrows: true,
        speed: 800,
        autoplay: true,
        vertical: true,
        autoplaySpeed: 5000,
        centerMode: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /* NewsTicker */
    $('#tweet-feed').slick({
        dots: false,
        arrows: true,
        speed: 800,
        autoplay: true,
        vertical: false,
        autoplaySpeed: 5000,
        centerMode: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /* NewsTicker */
    $('#bl-featured').slick({
        dots: true,
        arrows: false,
        speed: 800,
        autoplay: true,
        vertical: false,
        autoplaySpeed: 5000,
        centerMode: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /* Popular News */
    $('#pnews-slider').slick({
        arrows: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 3,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
                infinite: true
            }
        }, {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }]
    });

    /* Nicescroll */
    $("html").niceScroll();

    /* Nav-lava Lamp */
    $('#nav').spasticNav();

});

/* Simple tabs */
$('#tabs li a').on('click', function(e) {
    $('#tabs li, #content .current').removeClass('current').removeClass('fadeInLeft');
    $(this).parent().addClass('current');
    var currentTab = $(this).attr('href');
    $(currentTab).addClass('current fadeInLeft');
    e.preventDefault();

});

/* Responsive Menu */
$(".menu-trigger").on('click', function() {
    $("header nav").slideToggle("slow", function() {});
});

/* Backtotop */
$('.copy1 a').on('click', function() {
    $('html, body').animate({
        scrollTop: 0
    }, 'slow');
});

/* Flickr */
$(function() {
	$('#flickr').jflickrfeed({
	limit: 8,
	qstrings: {
		id: '52617155@N08'
	},
	itemTemplate: '<li><a href="{{image_b}}"><img src="{{image_s}}" alt="{{title}}" /></a></li>'
	});
});

// Google Map
$(function() {
    var map = new GMaps({
        el: "#map",
        lat: 40.714353,
        lng: -74.005973,
        zoom: 16,
        zoomControl: false,
        scrollwheel: false,
        controls: false,
        zoomControlOpt: {
            position: "TOP_LEFT"
        },
        panControl: false,
        streetViewControl: false,
        mapTypeControl: false,
        overviewMapControl: false,
        styles: [{
            "featureType": "road",
            "elementType": "labels",
            "styles": [{
                "visibility": "simplified"
            }, {
                "lightness": 20
            }]
        }, {
            "featureType": "administrative.land_parcel",
            "elementType": "all",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "landscape.man_made",
            "elementType": "all",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "transit",
            "elementType": "all",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "road.local",
            "elementType": "labels",
            "stylers": [{
                "visibility": "simplified"
            }]
        }, {
            "featureType": "road.local",
            "elementType": "geometry",
            "stylers": [{
                "visibility": "simplified"
            }]
        }, {
            "featureType": "road.highway",
            "elementType": "labels",
            "stylers": [{
                "visibility": "simplified"
            }]
        }, {
            "featureType": "poi",
            "elementType": "labels",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "road.arterial",
            "elementType": "labels",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "water",
            "elementType": "all",
            "stylers": [{
                "hue": "#a1cdfc"
            }, {
                "saturation": 30
            }, {
                "lightness": 49
            }]
        }, {
            "featureType": "road.highway",
            "elementType": "geometry",
            "stylers": [{
                "hue": "#f49935"
            }]
        }, {
            "featureType": "road.arterial",
            "elementType": "geometry",
            "stylers": [{
                "hue": "#fad959"
            }]
        }]
    });

    map.addMarker({
        lat: 40.714353,
        lng: -74.005973,
        icon: "images/marker.png"
    });
});
