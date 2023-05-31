import React, { useEffect, useRef, useState } from "react";
import "./chatbox.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faXmark,
  faMicrophone,
  faPaperPlane,
} from "@fortawesome/free-solid-svg-icons";
import { useSpeechRecognition, useSpeechSynthesis } from "react-speech-kit";
import ChatApi from "../../api/chatApi";
import Chat from "../chat/chat";

export default function ChatBox(props) {
  const [chatBoxValue, setChatBoxValue] = useState("");
  const [micActive, setMicActive] = useState(false);
  const locked = useRef(false);
  const inputRef = useRef(null);
  const divRef = useRef(null)
  const [chats, setChats] = useState([]);

  const { listen, listening, stop, supported } = useSpeechRecognition({
    onResult: (result) => {
      setChatBoxValue(result);
    },
  });

  const { speak } = useSpeechSynthesis();

  function updateChats(created_by, message, related = null) {
    setChats((chats) => [
      {
        created_by: created_by,
        message: message,
        related: related,
      },
      ...chats,
    ]);
    if (micActive && created_by === "server") {
      speak({ text: message });
    }
  }

  function onDataReceived(data) {
    setChatBoxValue("");
    if (data["status"] === 200) {
      const related = Object.values(data["related"]);
      if (related.length === 0) {
        updateChats("server", data["message"]);
      } else {
        updateChats("server", data["message"], related);
      }
    } else if (data["status"] === 400) {
      updateChats("server", data["message"]);
    }
    else {
      updateChats("server", data)
    }
    locked.current = false;
  }

  useEffect(() => {
    if(chats.length === 0) {
      ChatApi.direct_request("welcomegreeting").then(onDataReceived)
    }
    if(divRef.current){
      divRef.current.scrollTop = 0
    }
  }, [chats.length])

  return (
    <div
      className="chat-box-container flex flex-col"
      style={{
        height: props.isActive ? "550px" : 0,
        width: props.isActive ? "400px" : 0,
        opacity: props.isActive ? 1 : 0,
      }}
    >
      <div className="chat-box-top bg-red-800 h-11 w-full text-white flex items-center px-5">
        <h6 className="font-bold mx-2 text-xs">College Enquiry Chatbot</h6>
        <span className="flex-1" />
        <button
          className="speach-btn hover:scale-125 m-5"
          style={{
            color: micActive ? "green" : "white",
          }}
          onClick={() => {
            setMicActive(!micActive);
          }}
        >
          <FontAwesomeIcon
            className="text-xl speach-btn-icon"
            icon={faMicrophone}
          />
        </button>
        <button
          className="hover:text-red-400 hover:scale-125"
          onClick={() => props.toggle()}
        >
          <FontAwesomeIcon className="text-xl" icon={faXmark} />
        </button>
      </div>
      <div className="chat-box-middle flex-1" ref={divRef}>
        <div>
          {chats.map((item, index) => (
            <Chat
              key={index}
              data={item}
              onAction={(klass, text) => {
                if (locked.current) {
                  return;
                }
                locked.current = true;
                updateChats("client", text);
                ChatApi.direct_request(klass).then(onDataReceived);
              }}
            />
          ))}
        </div>
      </div>
      <div className="chat-box-bottom bg-red-800 h-16 w-full flex items-center justify-center p-3">
        <input
          type="text"
          className="text-sm"
          placeholder="Type Here!"
          autoCapitalize="false"
          value={chatBoxValue}
          onChange={(e) => setChatBoxValue(e.target.value)}
          ref={inputRef}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              if (locked.current) {
                return;
              }
              locked.current = true;
              updateChats("client", chatBoxValue);
              ChatApi.query_request(chatBoxValue).then(onDataReceived);
            }
          }}
        />
        <button
          className="s2t-mic-btn"
          style={{
            color: listening ? "red" : "black",
          }}
          onClick={() => {
            if (!supported) {
              alert("Sorry! But Your Browser Does Not Supports Voice Inputs");
              return;
            }
            if (listening) {
              stop();
              inputRef.current.focus();
            } else {
              listen();
            }
          }}
        >
          <FontAwesomeIcon className="s2t-mic-btn-icon" icon={faMicrophone} />
        </button>
        <button
          className="hover:text-red-500"
          onClick={() => {
            if (locked.current) {
              return;
            }
            locked.current = true;
            updateChats("client", chatBoxValue);
            ChatApi.query_request(chatBoxValue).then(onDataReceived);
          }}
        >
          <FontAwesomeIcon icon={faPaperPlane} />
        </button>
      </div>
    </div>
  );
}
