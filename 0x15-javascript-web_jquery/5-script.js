$('document').ready(function () {
  const list = $('ul.my_list');
  const add_item = $('#add_item');
  add_item.on('click', function () {
    $('<li>Item</li>').appendTo(list);
  });
});
