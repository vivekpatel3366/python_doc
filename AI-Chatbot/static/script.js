function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    // Display user message
    let userMessage = `<p><strong>You:</strong> ${userInput}</p>`;
    chatBox.innerHTML += userMessage;

    // Send message to backend
    fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            let botMessage = `<p><strong>Bot:</strong> ${data.response}</p>`;
            chatBox.innerHTML += botMessage;
            document.getElementById("user-input").value = ""; // Clear input field
        });
}