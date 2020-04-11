setTimeout(function() {
	$('.spinner').removeClass('visible').addClass('hidden');
	$('[data-fancybox="gallery"]').fancybox({
		maxWidth: 240,
		autoScale: true,
		buttons : [
	    	'close'
	  	]
	});
}, 1000);