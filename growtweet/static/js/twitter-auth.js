
function twitter_auth() {
  var form = $('#twitter-form');
  var url = form.attr('data-validate-username-url');
  $.ajax({
    url: url,
    type: 'POST',
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {

    }
  });
}
