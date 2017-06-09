
$(document).ready(function() {
    followers();
});


function followers() {
  var url = $("input.data-url-class").val();
  $.ajax({
    url: url,
    type: 'GET',
    timeout: 2*60*60*1000,
    dataType: 'json',
    success: function (data) {
        $('div.loading-field').html('<h1>It works!</h1>');
    },
    error: function (request, status, error) {
        $('div.loading-field').html('<h1>An error occurred</h1>');
    }
  });
}
