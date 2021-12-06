import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Login from "./Components/Login";
import Layout from "./Components/Layout";

function App() {
  return (
    <Router>
        <Routes>
          <Route  path="/" element={<Login/>}></Route>
        </Routes>
    </Router>
  );
}

export default App;
