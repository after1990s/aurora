// from http://stackoverflow.com/questions/11235206/twitter-bootstrap-form-file-element-upload-button
// Based in: http://duckranger.com/2012/06/pretty-file-input-field-in-bootstrap/
// Use:
//     <input id="document_field" type="file" data-label="Choose Document">
//     <script> $("#document_field").niceFileField(); </script>
//
(function( $ ) {
  $.fn.niceFileField = function() {
    this.each(function(index, file_field) {
      file_field = $(file_field);
      var label = file_field.attr("data-label") || "Choose File";

      //file_field.css({"visibility": "hidden"});
      file_field.css({"position": "absolute"});
      file_field.css({"top": "-1000px"});
      file_field.after("<div class=\"nice_file_field input-append\"><input class=\"input span9\" type=\"text\"><a class=\"btn\">" + label + "</a></div>");

      var nice_file_field = file_field.next(".nice_file_field");
      console.log("nice_file_field", nice_file_field)
      nice_file_field.find("a").click( function(){ file_field.click() } );
      file_field.change( function(){
        nice_file_field.find("input").val(file_field.val());
      });
    });
  };
})( jQuery );

$('input[type=file]').each(function() {
    $(this).niceFileField();
});

// multiple1902: my modifications:
// changed 'display: none' to 'position: absolute; top: -1000px', 
//   because a file input with 'display: none' doesn't response to 
//   a external 'click' function call.
