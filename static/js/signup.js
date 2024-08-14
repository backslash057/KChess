var outputElt = document.querySelector(".output");
var formElt = document.querySelector(".form");
var usernameElt = document.querySelector("#username");
var passwordElt = document.querySelector("#password");
var rememberElt = document.querySelector("#remember");
var submitElt = document.querySelector("#submit");


formElt.addEventListener('submit', (e)=>{
	e.preventDefault();

	outputElt.style.display = "none";
	submitElt.classList.toggle('waiting');


	
	fetch("/signup", {
		method: 'POST',
		body: JSON.stringify({
			username: usernameElt.value,
			password: passwordElt.value,
			remember: rememberElt.value
		}),
		headers: {
	        'Content-Type': 'application/json'
	    }
	})
	.then(response => response.json())
	.then(response => {
		if(response.success) {
			outputElt.classList.add('green');
			outputElt.innerText = "Signup successful.";
			setTimeout(()=> {
				window.location.href = "/";
			}, 1000);
		}
		else {
			outputElt.innerText = response.message;
		}
		outputElt.style.display = "block";
		submitElt.classList.toggle('waiting');
	})
	.catch(error => {
		outputElt.innerText = "An error occured. Try later";
		outputElt.style.display = "block";
		submitElt.classList.toggle('waiting');
	})
});