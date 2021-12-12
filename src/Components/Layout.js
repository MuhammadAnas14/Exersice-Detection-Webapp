import React from "react";
import Navbar from "./Navbar";
import "./CSS/layout.css";
import Home from './home'

const Layout = (props) => {
  return (
    <div>
      <header className="sticky-top">
        <Navbar />
      </header>
      <main className="main-content"><Home/></main>
    </div>
  );
};
export default Layout;