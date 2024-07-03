board = document.querySelector(".board");

chatInput = document.querySelector('.chat-input');

chatInput.addEventListener('keydown', (e)=> {
    if(e.keyCode == 13) { // Return keyCode
        sendMesssage(chatInput.value)
    }
});


function sendMessage(message) {
    fetch("/game",{
            method: "POST",
            headers: {
                "Content-Type": "aplication/json"
            },
            body: JSON.stringify({'message': message})
        }
    )
    .then(response => response.json())
    .then(response => {
        console.log(response)
    });
}