let API_KEY = "d1f3dd3d-cc92-4827-bef2-68938e6943ba";

$.ajax({
	type: "GET",
  	beforeSend: function(request) {
    	request.setRequestHeader("X-Api-Key", API_KEY);
  	},
  	url: "https://api.thecatapi.com/v1/images/search?size=thumb&limit=10&mime_types=jpg",
  	processData: false,
  	success: function(response) {
  		$('.spinner').removeClass('visible').addClass('hidden');
		processCatsResponse(response);
  	}
});

function catObjToElement(catObj) {
	let catId = catObj.id;
	let url = catObj.url;

	return '<a data-fancybox="gallery" href="'+ url +'"><img src="' + url +'"></a>'
}

function processCatsResponse(json) {
	for (i = 0; i < json.length; i++) { 
		let catObj = json[i];
		var text = $('#images').html();
		text += catObjToElement(catObj);
		$('#images').html(text);
	}
	$('[data-fancybox="gallery"]').fancybox({
		maxWidth: 240,
		autoScale: true,
		buttons : [
	    	'close'
	  	]
	});
}