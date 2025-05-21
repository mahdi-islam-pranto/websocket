window.addEventListener("DOMContentLoaded", () => {
  // Create a list element to show messages
  const messages = document.createElement("ul");
  document.body.appendChild(messages);

  // Create WebSocket connection  
const websocket = new WebSocket("ws://localhost:5678/");
  
// Handle incoming messages
  websocket.onmessage = ({ data }) => {
    const message = document.createElement("li");
    const content = document.createTextNode(data);
    message.appendChild(content);
    messages.appendChild(message);
  };


  // handle stop button
document.getElementById("stop").addEventListener("click", () => {
  // close the websocket connection
  websocket.close();
  
});
});

