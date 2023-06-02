$('document').ready(function () {
  const btn_translate = s$('#btn_translate');
  const language_code = $('#language_code').val();
  const hello = $('#hello');
  btn_translate.on('click', function () {
    const code = language_code.val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/',
      data: { lang: code },
      method: 'GET',
      dataType: 'json',
      success: function (response) {
        hello.text(response.hello);
      },
      error: function (xhr, status, error) {
        console.error('something went wrong', error);
      }
    });
  });
});
