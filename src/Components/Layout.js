import React from "react";
import Navbar from "./Navbar";
import "./CSS/layout.css";

const Layout = (props) => {
  return (
    <div>
      <header className="sticky-top">
        <Navbar />
      </header>
      <main className="main-content">{props.children}</main>
    </div>
  );
};
export default Layout;