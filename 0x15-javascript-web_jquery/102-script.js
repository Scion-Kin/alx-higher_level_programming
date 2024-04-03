$(function () {
  $('INPUT#btn_translate').click(function () {
    const langChoice = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: langChoice, 
      success: function(data, textStatus) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
