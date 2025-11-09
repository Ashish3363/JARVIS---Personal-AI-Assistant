// import React, { useState } from "react";
// import "./styles.css";

// function App() {
//   const [messages, setMessages] = useState([]);
//   const [input, setInput] = useState("");

//   const sendMessage = async () => {
//     if (!input) return;

//     // Add user message to chat
//     const newMessages = [...messages, { sender: "user", text: input }];
//     setMessages(newMessages);

//     // Call backend API
//     try {
//       const res = await fetch("http://127.0.0.1:8000/chat", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ question: input }),
//       });

//       const data = await res.json();
//       setMessages([
//         ...newMessages,
//         { sender: "ai", text: data.answer || "No answer returned." },
//       ]);
//       setInput("");
//     } catch (err) {
//       console.error(err);
//       setMessages([...newMessages, { sender: "ai", text: "Error occurred." }]);
//     }
//   };

//   const handleKeyPress = (e) => {
//     if (e.key === "Enter") sendMessage();
//   };

//   return (
//     <div className="chat-container">
//       <h1>Personal AI Chat</h1>
//       <div className="chat-box">
//         {messages.map((msg, idx) => (
//           <div
//             key={idx}
//             className={`chat-message ${msg.sender === "user" ? "user" : "ai"}`}
//           >
//             <strong>{msg.sender === "user" ? "You" : "AI"}: </strong>
//             {msg.text}
//           </div>
//         ))}
//       </div>
//       <div className="input-box">
//         <input
//           type="text"
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           onKeyDown={handleKeyPress}
//           placeholder="Type your question..."
//         />
//         <button onClick={sendMessage}>Send</button>
//       </div>
//     </div>
//   );
// }

// export default App;



// import React, { useState } from "react";
// import "./styles.css";

// function App() {
//   const [question, setQuestion] = useState("");
//   const [answer, setAnswer] = useState("");
//   const [sources, setSources] = useState("");

//   const ask = async () => {
//     if (!question) return;

//     try {
//       const response = await fetch("http://127.0.0.1:8000/chat", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ question }),
//       });

//       const data = await response.json();
//       setAnswer(data.answer);
//       setSources(data.sources || "No sources provided");
//     } catch (error) {
//       setAnswer("Error: " + error.message);
//       setSources("");
//     }
//   };

//   return (
//     <div style={{ padding: "20px", fontFamily: "Arial" }}>
//       <h2>Ask your AI Assistant</h2>
//       <textarea
//         rows="4"
//         cols="60"
//         value={question}
//         onChange={(e) => setQuestion(e.target.value)}
//       ></textarea>
//       <br />
//       <button onClick={ask} style={{ marginTop: "10px" }}>
//         Ask
//       </button>
//       <h3>Answer:</h3>
//       <pre>{answer}</pre>
//       <h3>Sources:</h3>
//       <pre>{sources}</pre>
//     </div>
//   );
// }

// export default App;



// import React, { useState } from "react";
// import "./styles.css";


// function App() {
//   const [input, setInput] = useState("");
//   const [messages, setMessages] = useState([]);

//   const sendMessage = async () => {
//     if (!input.trim()) return;

//     // Add user message
//     const newMessages = [...messages, { role: "user", text: input }];
//     setMessages(newMessages);

//     setInput("");

//     // Send to backend
//     const response = await fetch("http://127.0.0.1:8000/ask", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ question: input })
//     });

//     const data = await response.json();

//     // Add AI answer
//     setMessages([...newMessages, { role: "assistant", text: data.answer }]);
//   };

//   return (
//     <div className="chat-container">
//       <div className="chat-window">
//         {messages.map((msg, i) => (
//           <div key={i} className={`message ${msg.role}`}>
//             {msg.text}
//           </div>
//         ))}
//       </div>

//       <div className="input-area">
//         <input
//           type="text"
//           placeholder="Ask Jarvis..."
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           onKeyDown={(e)=> e.key==="Enter" && sendMessage()}
//         />
//         <button onClick={sendMessage}>➤</button>
//       </div>
//     </div>
//   );
// }

// export default App;



import React, { useState } from "react";
import "./styles.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [darkMode, setDarkMode] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", text: input }];
    setMessages(newMessages);
    setInput("");

    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: input })
    });

    const data = await response.json();

    setMessages([...newMessages, { role: "assistant", text: data.answer }]);
  };

  return (
    <div className={`main-wrapper ${darkMode ? "dark" : ""}`}>
      
      {/* Theme Toggle Button */}
      <button className="theme-toggle" onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "☀️" : "🌙"}
      </button>

      <h1 className="title">JARVIS</h1>
      <p className="subtitle">Your Personal Assistant</p>

      <div className="chat-container">
        <div className="chat-window">
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              {msg.text}
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Send a message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>➤</button>
        </div>
      </div>
    </div>
  );
}

export default App;

