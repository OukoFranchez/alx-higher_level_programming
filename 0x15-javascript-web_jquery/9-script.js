$('document').ready(function() {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	$.get(url, (data, status) => {
		$('div#hello').text(data.hello);
	});
});