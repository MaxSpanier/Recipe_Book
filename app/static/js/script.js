$(document).ready(function() {
	var max_fields      = 15; //maximum input boxes allowed
	var wrapper   		= $(".input_fields_wrap"); //Fields wrapper
	var add_button      = $(".add_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
            $(wrapper).append('<div><input style="float: left;" type="text" name="ingredient" style="width:80%;" placeholder="Extra Ingredients"/><a class="remove_field"><i class="fa fa-times-circle fa-2x"varia-hidden="true"></a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});