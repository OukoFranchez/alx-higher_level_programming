$('document').ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</Item>');

    $('ul.my_list').append(newItem);
  });
});
