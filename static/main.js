// $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

$( function() {
  $("#text-container").mouseup(
      function() {
          var selectedText = window.getSelection().toString();
          var splitName = selectedText.split(" ")
          if (splitName.length === 2) {
            $('#first_name').val(toTitleCase(splitName[0]));
            $('#last_name').val(toTitleCase(splitName[1]));
          }
          else {
            $('#first_name').val('');
            $('#last_name').val('');
          }
          $('#name').val(selectedText);
          $('#title').val('');
          $('#comments').val('');
        });
});

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}
