import React from "react";
import "./CSS/home.css";
import { Container, Card, Row, Col } from "react-bootstrap";
import pushUp from './Assets/push-up.png'
import biceps from './Assets/biceps.png'
import Shoulder from './Assets/shoulder.png'

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
            <Card.Img variant="top" className ="image-icon" src = {biceps} />
            <Card.Body>
              <Card.Title>Card Title</Card.Title>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card style={{ width: "18rem" }}>
            <Card.Img variant="top" className ="image-icon" src = {pushUp}  />
            <Card.Body>
              <Card.Title>Card Title</Card.Title>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card style={{ width: "18rem" }}>
            <Card.Img variant="top" className ="image-icon" src = {Shoulder} />
            <Card.Body>
              <Card.Title>Card Title</Card.Title>
            </Card.Body>
          </Card>
        </Col>
      </Row>
      </div>
    </Container>
  );
};

export default Home;
