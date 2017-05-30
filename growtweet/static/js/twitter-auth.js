
function twitter_auth() {
  var form = $('#twitter-form');
  $.ajax({
    url: '/',
    type: 'POST',
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {
        alert(data);
    }
  });
}
