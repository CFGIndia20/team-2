// Send complain

$(document).ready(function(){
	$("#id_mobileNumber").attr("placeholder", "Enter your Mobile No.");
	$("#id_description").attr("placeholder", "Enter your Complaint");
	$("#id_location").attr("placeholder", "Enter your Location");


	// $(".complain-btn").on("click", function(){
	// 	var mobile = $("#mobile").val();
	// 	if(!$('#mobile').val().match('[0-9]{10}'))  {
    //         alert("Please put 10 digit mobile number");
    //         return;
    //     }

	// 	var complain = $("#complain-text").val();
	// 	var location = $("#location").val();
		
	// 	$.post("",{mobile: mobile, complain:complain, location:location}, function(msg){
	// 		console.log(msg);
	// 	});
	// });
});