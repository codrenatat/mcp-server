function App() {
  const [conversations, setConversations] = React.useState([]);
  const [selectedId, setSelectedId] = React.useState(null);

  React.useEffect(() => {
    fetch("http://localhost:3000/conversations")
      .then(res => res.json())
      .then(data => {
        setConversations(data);
        if (data.length > 0) setSelectedId(data[0].id);
      });
  }, []);

  return (
    <div className="container">
      <Sidebar
        conversations={conversations}
        onSelect={setSelectedId}
        selectedId={selectedId}
      />
      <ChatWindow conversationId={selectedId} />
    </div>
  );
}
