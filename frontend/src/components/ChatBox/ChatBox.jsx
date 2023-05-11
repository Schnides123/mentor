import React, { useState, useRef } from 'react';
import styles from './ChatBox.css';
import { ChatMessage } from '../ChatMessage/ChatMessage';
import { ChatInput } from '../ChatInput/ChatInput';
import sendQuery from '../../services/QueryService';


export function ChatBox() {

  const [history, setHistory] = useState([{message:"**Hello**, what can I help you with today?", sender:"bot"}]);

  const promptRef = useRef('How do I exit vim?');

  const addChatMessages = (newMessages) => {
    console.log(newMessages)
    setHistory([...history, ...newMessages]);
  }

  const handleSend = () => {
    prompt = promptRef.current.value
    console.log(prompt)
    console.log(history)
    sendQuery(prompt, (message)=>addChatMessages([{message: prompt, sender: "user"},{message: message, sender: "bot"}]));
  }


  return (
  <div className="flex flex-grow border-2 border-pink overflow-scroll">
    <div className="w-full max-h-[90%] overflow-scroll">
      {history.map((message, index) => <ChatMessage message={message.message} sender={message.sender} key={index}></ChatMessage>)}
    </div>
    <ChatInput promptRef={promptRef} handleSend={handleSend}></ChatInput>
  </div>
  );
}
