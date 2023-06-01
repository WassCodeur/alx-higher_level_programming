$('document').ready(function () {
  const header = $('header');
  const update_header = $('#update_header');
  update_header.on('click', function () {
    header.text('New Header!!!');
  });
});
