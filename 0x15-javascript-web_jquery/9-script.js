$('document').ready(function () {
  const hello = $('#hello');
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      hello.text(response.hello);
    },
    error: function (xhr, status, error) {
      console.error('Oooh, something went wrong', error);
    }
  });
});
