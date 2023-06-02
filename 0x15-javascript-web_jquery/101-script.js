$('document').ready(function () {
  const my_list = $('ul.my_list');
  const add_item = $('#add_item');
  const remove_item = $('#remove_item');
  const clear_list = $('#clear_list');
  add_item.on('click', function () {
    $('<li>Item</li>').appendTo(my_list);
  });
  remove_item.on('click', function () {
    $('ul.my_list li:last-child').remove();
  });
  clear_list.on('click', function () {
    my_list.empty();
  });
});
