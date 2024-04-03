$(function () {
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which == 13) {
      const langChoice = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
      $.ajax({
        type: 'GET',
        url: langChoice, 
        success: function(data, textStatus) {
          $('DIV#hello').text(data.hello);
        }
      });
    }
  });
  $('INPUT#btn_translate').on('click', function(event) {
    $('INPUT#language_code').trigger('keypress');
  });
});
