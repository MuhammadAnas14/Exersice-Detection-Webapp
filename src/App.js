import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Login from "./Components/Login";
import Layout from "./Components/Layout";
import Video from './Components/video'

function App() {
  return (
    <Router>
        <Routes>
          <Route  path="/" element={<Login/>}></Route>
          <Route path= "/main" element={<Layout/>} />
          <Route path="/video" element={<Video/>} />
        </Routes>
    </Router>
  );
}

export default App;
