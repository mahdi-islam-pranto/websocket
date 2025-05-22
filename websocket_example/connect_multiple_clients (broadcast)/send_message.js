
window.addEventListener("DOMContentLoaded", () => {
  // Create a ul list element to show messages
  const messages = document.createElement("ul");
  document.body.appendChild(messages);

  // Create WebSocket connection
  const websocket = new WebSocket("ws://localhost:5000/");

  // Handle incoming messages
  websocket.onmessage = ({ data }) => {
    const message = document.createElement("li");
    const content = document.createTextNode(data);
    message.appendChild(content);
    messages.appendChild(message);
  };

  // send message to server
  document.getElementById("send_message").addEventListener("click", () => {
    const message = document.getElementById("message_id").value;
    // send message to server
    websocket.send(message);
    console.log("message sent" + message);
  });


  // handle stop button
  document.getElementById("stop").addEventListener("click", () => {
    // close the websocket connection
    websocket.close();
  });
});