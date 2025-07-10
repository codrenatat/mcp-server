function ChatWindow({ conversationId }) {
  const [messages, setMessages] = React.useState([]);
  const [input, setInput] = React.useState("");

  React.useEffect(() => {
    if (!conversationId) return;

    fetch(`http://localhost:3000/messages/${conversationId}`)
      .then(res => res.json())
      .then(data => setMessages(data));
  }, [conversationId]);

  const sendMessage = () => {
    if (!input.trim()) return;

    const newMsg = {
      conversationId,
      role: "user",
      content: input.trim(),
    };

    setMessages(prev => [...prev, { ...newMsg, id: Date.now().toString() }]);
    setInput("");

    fetch("http://localhost:3000/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newMsg),
    });

    fetch("http://localhost:3000/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        conversationId,
        role: "assistant",
        content: `Simulando respuesta a: "${newMsg.content}"`,
      }),
    })
      .then(res => res.json())
      .then(data => setMessages(prev => [...prev, data]));
  };

  return (
    <div className="chatwindow">
      <div className="messages">
        {messages.map(msg => (
          <div
            key={msg.id}
            className={`message ${msg.role === "user" ? "user" : "assistant"}`}
          >
            {msg.content}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
          placeholder="Escribe tu mensaje..."
          autoFocus
        />
        <button onClick={sendMessage}>Enviar</button>
      </div>
    </div>
  );
}