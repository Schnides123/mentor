import React from 'react';
import ReactMarkdown from 'react-markdown';
export function ChatMessage({message, sender="bot"}) {
  return (
    <div className="w-full grid grid-cols-4 gap-4 p-4">
    <div className={sender === "bot" ? "col-start-1 col-span-3" : "col-start-2 col-span-3"}>
    <div className={sender === "bot" ? "rounded-lg bg-mauve/75 max-w-3/4 p-2" : "rounded-lg bg-peach/75 max-w-3/4 p-2"}>
      <ReactMarkdown className="text-white">
        {message}
      </ReactMarkdown>
    </div>
    </div>
    </div>
  );
}
