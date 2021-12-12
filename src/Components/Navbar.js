import React from "react";
import {  Navbar, Container, Image } from "react-bootstrap";
import "./CSS/layout.css";
import Logo from "./Assets/logo.png";
import Logo2 from "./Assets/logo2.png"

const Head = () => {

  return (
    <Navbar
      variant="light"
      expand="lg"
      style={{
        transition: "0.7s ease-in-out",
        backgroundColor: "transparent",
        height:90
      }}
    >
      <Container>
        <Navbar.Brand href="/main" style={{ position: "absolute", left: 100 }}>
          <Image
            src={Logo}
            className="shadowed"
            style={{
              backgroundColor: "transparent",
            }}
            fluid
          />
        </Navbar.Brand>
        <Navbar.Collapse id="basic-navbar-nav" className="NavSpace">
        <Image
            src={Logo2}
            className="shadowed"
            style={{
              backgroundColor: "transparent",
            }}
            fluid
          />
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Head;