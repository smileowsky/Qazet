$(document).ready(function() {
    function close_accordion_section() {
        $('.accordion-p .accordion-section-title').removeClass('active');
        $('.accordion-p .accordion-section-content').slideUp(500).removeClass('open');
    }
 
    $('.accordion-section-title').click(function(e) {
        // Grab current anchor value
        var currentAttrValue = $(this).attr('href');
 
        if($(this).is('.active')) {
            close_accordion_section();

        }else {
            close_accordion_section();
 
            // Add active class to section title
            $(this).addClass('active');
            // Open up the hidden content panel
            $('.accordion-p ' + currentAttrValue).slideDown(600).addClass('open');
        }
 
        e.preventDefault();
    });
});