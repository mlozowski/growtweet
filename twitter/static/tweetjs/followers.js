
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
        $('div.loading-field').html(create_table(data));
    },
    error: function (request, status, error) {
        $('div.loading-field').html('<h1>An error occurred</h1>');
    }
  });
}


function create_table(data) {
    var table = "" +
    "<table border=1>" +
      "<thead>" +
        "<tr>" +
          "<th>Follower of my followers</th>" +
          "<th>Number of my followers</th>" +
        "</tr>" +
      "</thead>" +
      "<tbody>";

    $.each( data.result, function( key, value ) {
      table += "<tr>";
      table += "<td>" + value.follower_follower_name + "</td>";
      table += "<td>" + value.followers_count + "</td>";
      table += "</tr>";
    });

    table += "" +
      "</tbody>" +
    "</table>";

    return table;
}
