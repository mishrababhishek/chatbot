import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRocketchat } from "@fortawesome/free-brands-svg-icons";
import "./App.css";
import Info from "./components/info/info";
import ChatBox from "./components/chatbox/chatbox";

function App() {
  const [chatboxState, setChatboxState] = useState(false);

  function toggleChatWindow(newState) {
    setChatboxState(newState);
  }

  return (
    <div className="h-screen w-screen flex flex-col bg-custom-image items-start justify-start">
      <Info className="text-white mt-32 ml-32" />
      <button className="control-button">
        <FontAwesomeIcon
          icon={faRocketchat}
          onClick={() => toggleChatWindow(true)}
        />
      </button>
      <ChatBox
        isActive={chatboxState}
        toggle={() => toggleChatWindow(false)}
      />
    </div>
  );
}

export default App;
