// starter JavaScript for disabling form submissions if there are invalid fields
(function () {
	'use strict'
	// Fetch all the forms we want to apply custom Bootstrap validation styles to
	var forms = document.querySelectorAll('.needs-validation')
  
	// Loop over them and prevent submission
	Array.prototype.slice.call(forms)
	  .forEach(function (form) {
		form.addEventListener('submit', function (event) {
		  if (!form.checkValidity()) {
			event.preventDefault()
			event.stopPropagation()
		  }

		  form.classList.add('was-validated')
		}, false)
	  })
})();


function copyTextFunction() {
	/* Get the text field */
	var copyText = document.getElementById("cmd");
  
	/* Select the text field */
	copyText.select();
	copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
	 /* Copy the text inside the text field */
	navigator.clipboard.writeText(copyText.value);
  
	/* Alert the copied text */

	
	btnName = document.getElementById("copyBtn");
	btnName.value = "copied";
	setTimeout(function(){
		btnName.value = "copy";
	}, 1500);
}





