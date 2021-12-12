import React from "react";
import "./CSS/home.css";
import { Container, Card, Row, Col, Button } from "react-bootstrap";
import pushUp from "./Assets/push-up.png";
import biceps from "./Assets/biceps.png";
import Shoulder from "./Assets/shoulder.png";
import {Link } from "react-router-dom";


const Home = () => {
  return (
    <Container>
      <div className="wrapper">
        <h3 className="head">Which excercise would you like to do today?</h3>
      </div>

      <div className="wrapper2">
        <Row>
          <Col>
            <Card style={{ width: "18rem" }}>
              <Card.Img variant="top" className="image-icon" src={biceps} />
              <Card.Body>
                <Card.Title>Biceps Curl</Card.Title>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card style={{ width: "18rem" }}>
              <Card.Img variant="top" className="image-icon" src={pushUp} />
              <Card.Body>
                <Card.Title>Push Ups</Card.Title>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card style={{ width: "18rem" }}>
              <Card.Img variant="top" className="image-icon" src={Shoulder} />
              <Card.Body>
                <Card.Title>Shoulder Press</Card.Title>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </div>
      <div className="wrapper3">
      <Link to="/video"><Button variant="primary">Confirm</Button></Link>
      </div>
    </Container>
  );
};

export default Home;
