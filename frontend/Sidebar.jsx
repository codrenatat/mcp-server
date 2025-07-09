function Sidebar({ conversations, onSelect, selectedId }) {
  return (
    <div className="sidebar">
      <h2>Conversaciones</h2>
      <ul>
        {conversations.map(c => (
          <li
            key={c.id}
            className={selectedId === c.id ? "selected" : ""}
            onClick={() => onSelect(c.id)}
          >
            {c.title}
          </li>
        ))}
      </ul>
    </div>
  );
}
