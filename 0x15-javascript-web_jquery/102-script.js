$(document).ready(() => {
	$('input#btn_translate').click(() => {
		const url = 'https://www.fourtonfish.com/hellosalut/hello/';
		$.get(url, (data, status) => {
			$('div#hello').text(data.hello);
		});
	});
});