$('document').ready(function () {
  const header = $('header');
  const div = $('#toggle_header');
  div.on('click', function () {
    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    }
  });
});
