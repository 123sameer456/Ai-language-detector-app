function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    var chatMessages = document.getElementById("chat-messages");
    var chatbox = document.getElementById("chatbox");

    // Display user message
    var userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerHTML = "<strong>You:</strong> " + userMessage;
    chatMessages.appendChild(userDiv);

    // Send message to server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        var botDiv = document.createElement("div");
        botDiv.className = "bot-message";
        botDiv.innerHTML = "<strong>Bot:</strong> " + data.message;
        chatMessages.appendChild(botDiv);

        // Display menu prompt
        chatMessages.innerHTML += "<div class='menu-prompt'>" + data.menu_prompt + "</div>";

        // Scroll to bottom
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    // Clear user input
    document.getElementById("user-input").value = "";
}
