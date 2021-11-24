import React from "react";
import { Nav, Navbar, Container, Image } from "react-bootstrap";
import "./CSS/layout.css";
// import Logo from "../Assets/logo2.png";
// import Logo from "../Assets/default-monochrome.svg"
import { useState, useRef, useEffect } from "react";

const Head = () => {
  let authButton;
  let user = localStorage.getItem("user");

  const handlelogout = () => {
    localStorage.clear("user");
  };

  if (user) {
    authButton = (
      <Nav.Link href="/Login" onClick={handlelogout}>
        Logout
      </Nav.Link>
    );
  } else {
    authButton = <Nav.Link href="/login">Login</Nav.Link>;
  }

  const [navBackground, setNavBackground] = useState(false);
  const [navOpacity, setNavOpacity] = useState(false);
  const [navShadow, setNavShadow] = useState(false);
    const [logoBackground, setLogoBackground] = useState(false);
  const navRef = useRef();
  navRef.current = navBackground;
  navRef.current = navOpacity;
  navRef.current = navShadow;
  navRef.current = logoBackground;
  useEffect(() => {
    const handleScroll = () => {
      const show = window.scrollY > 50;
      if (navRef.current !== show) {
        setNavBackground(show);
        setNavOpacity(show);
        setNavShadow(show);
        setLogoBackground(show);
      }
    };
    document.addEventListener("scroll", handleScroll);
    return () => {
      document.removeEventListener("scroll", handleScroll);
    };
  }, []);
  return (
    <Navbar
      variant="light"
      expand="lg"
      style={{
        transition: "0.7s ease-in-out",
        backgroundColor: navBackground ? "rgb(254, 252, 232)" : "transparent",
        opacity: navOpacity ? 0.85 : 1,
        height: 90,
        boxShadow: navShadow
          ? "0 2px 4px 0 rgba(0,0,0,.2)"
          : "0 2px 4px 0 rgba(0,0,0,0)",
      }}
    >
      <Container>
        <Navbar.Brand href="/" style={{ position: "absolute", left: 100 }}>
          {/* <Image
            src={Logo}
            className="shadowed"
            style={{
              backgroundColor: navBackground ? "transparent" : "#025469",
            }}
            fluid
          /> */}
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav" className="NavSpace">
          <Nav className="mr-auto ">
            {/* <Nav.Link href="/home">home</Nav.Link> */}
            <Nav.Link href="/detection">Detection</Nav.Link>
            {authButton}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Head;