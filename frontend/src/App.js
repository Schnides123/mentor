import logo from './logo.svg';
import './App.css';
import { ChatBox } from './components/ChatBox/ChatBox';

function App() {
  return (
    <div className="container-xl justify-center flex flex-col h-screen p-4 bg-gradient-to-b from-base to-crust" >
      <div className="flex justify-center">
      <header className="justify-center items-center">
        <h1 className="font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-r from-pink to-mauve">Mentor</h1>
        <h2 className="text-center text-2xl text-subtext0">Ask Me Anything!</h2>
      </header>
      </div>
      <ChatBox></ChatBox>
    </div>
  );
}

export default App;
