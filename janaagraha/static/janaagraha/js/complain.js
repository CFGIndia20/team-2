// Send complain

$(document).ready(function(){
	$(".complain-btn").on("click", function(){
		var mobile = $("#mobile").val();
		if(!$('#mobile').val().match('[0-9]{10}'))  {
            alert("Please put 10 digit mobile number");
            return;
        }
		var complain = $("#complain-text").val();
		$.post("",{mobile: mobile, complain:complain}, function(msg){
			console.log(msg);
		});
	});
});