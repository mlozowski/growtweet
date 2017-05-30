
function twitter_auth() {
  var form = $('#twitter-form');
  var url = form.attr('data-validate-username-url');
  $.ajax({
    url: url,
    type: 'POST',
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {

    },
    error: function (request, status, error) {
        data = JSON.parse(request.responseText);
        if (data.username != undefined) {
            alert(data.username);
        }
        if (data.password != undefined) {
            alert(data.password)
        }
    }
  });
}
