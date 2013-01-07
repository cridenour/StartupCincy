function imgError(image) {
	image.onerror = '';
	image.src = '/img/placeholder.jpg'
	return true;
}

$(function() {
	$(".carousel").carousel();
})