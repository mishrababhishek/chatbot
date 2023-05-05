import React from "react";
import "./info.css";

export default function Info(props) {
  const { className } = props
  return (
    <div className={className}>
      <p className="font-bold text-5xl mb-1">JIT BOT 🤖</p>
      <p className="whitespace-normal w-1/2 text-sm mb-4">
        The JIT Chat bot is a web application that answers students' basic
        queries about their college program. It uses Natural Language Processing
        to understand and respond to user queries, and is built using Python's
        TensorFlow library, FastAPI, Uvicorn, React, and Tailwind CSS. The
        frontend is designed with a modern interface using React and Tailwind
        CSS, while the backend utilizes FastAPI and Uvicorn for fast and
        efficient handling of requests. The chatbot is customizable, allowing
        colleges to tailor the bot's responses to their specific requirements.
      </p>
      <p className="font-extrabold mb-3">Component Used to Build Are :-</p>
      <ul>
        <li>
          <div className="flex">
            <p className="font-semibold mr-1">Python's TensorFlow library</p>:-
            used for Natural Language Processing (NLP) to understand and respond
            to the user's queries.
          </div>
        </li>
        <li>
          <div className="flex">
            <p className="font-semibold mr-1">FastAPI</p> :- a modern, fast, web
            framework for building APIs with Python.
          </div>
        </li>
        <li>
          <div className="flex">
            <p className="font-semibold mr-1">Uvicorn</p> :- an ASGI web server
            that provides lightning-fast server performance.
          </div>
        </li>
        <li>
          <div className="flex">
            <p className="font-semibold mr-1">React</p> :- a popular JavaScript
            library for building user interfaces.
          </div>
        </li>
        <li>
          <div className="flex">
            <p className="font-semibold mr-1">Tailwind CSS</p> :- a
            utility-first CSS framework used to design and style the user
            interface.
          </div>
        </li>
      </ul>
    </div>
  );
}
