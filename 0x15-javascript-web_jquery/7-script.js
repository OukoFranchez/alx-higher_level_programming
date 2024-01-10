$('document').ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function () {
      $('#character').text(data.name);
    },
    error: function () {
      console.error('Error fetching character data');
    }
  });
});
