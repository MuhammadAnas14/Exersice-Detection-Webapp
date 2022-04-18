import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Login from "./Components/Login";
import Layout from "./Components/Layout";
import Video from './Components/video'
import Video1 from './Components/video1';
import Video2 from './Components/video2';

function App() {
  return (
    <Router>
        <Routes>
          <Route  path="/" element={<Login/>}></Route>
          <Route path= "/main" element={<Layout/>} />
          <Route path="/video" element={<Video/>} />
          <Route path="/video1" element={<Video1/>} />
          <Route path="/video2" element={<Video2/>} />
        </Routes>
    </Router>
  );
}

export default App;
