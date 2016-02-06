// back to top button from http://html-tuts.com/back-to-top-button-jquery/

var amountScrolled = 300;

$(window).scroll(function() {
	if ( $(window).scrollTop() > amountScrolled){
		$('.back-to-top').fadeIn(1000);
		$('.menu-background').addClass('fixed-menu');
	} else {
		$('.back-to-top').fadeOut('slow');
		$('.menu-background').removeClass('fixed-menu')
	}
});

$('.back-to-top').click(function() {
	$('body, html').animate({
		scrollTop: 0
	}, 700);
	return false;
});

//These three pieces are to offset the page when using the menu to jump
//to an anchored point on the page.
//From this thread - http://stackoverflow.com/questions/17534661/make-anchor-link-go-some-pixels-above-where-its-linked-to

function offsetAnchor() {
    if(location.hash.length !== 0) {
        window.scrollTo(window.scrollX, window.scrollY - 80);
    }
}

// This will capture hash changes while on the page
$(window).on("hashchange", function () {
    offsetAnchor();
});

// This is here so that when you enter the page with a hash,
// it can provide the offset in that case too. Having a timeout
// seems necessary to allow the browser to jump to the anchor first.
window.setTimeout(function() {
    offsetAnchor();
}, 1); // The delay of 1 is arbitrary and may not always work right (although it did in my testing).