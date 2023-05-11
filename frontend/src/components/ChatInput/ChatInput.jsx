import React from 'react';

import styles from './ChatInput.css';


export function ChatInput({promptRef, handleSend}) {

  return (
    <div className="absolute left-0 bottom-0 w-full px-8 py-8">
  <div className="flex items-center py-2 px-1 bg-surface0">
    <input className="appearance-none bg-transparent border-none w-full text-text mr-3 py-1 px-1 leading-tight focus:outline-none" type="text" placeholder="How do I exit vim?" ref={promptRef} />
    <button className="flex-shrink-0 bg-surface2 hover:text-white  hover:border-white text-sm border-2 border-peach text-peach mx-1 py-1 px-2 rounded" type="button" onClick={handleSend}>
      Send
    </button>
  </div>
  </div>
  );
}
