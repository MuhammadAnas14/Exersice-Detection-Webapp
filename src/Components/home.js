import React ,{useState} from "react";
import "./CSS/home.css";
import { Container, Card, Row, Col, Button } from "react-bootstrap";
import {useNavigate} from 'react-router-dom'
import pushUp from "./Assets/push-up.png";
import biceps from "./Assets/biceps.png";
import Shoulder from "./Assets/shoulder.png";

const Home = () => {

  const [Exercise, setExercise] = useState("");

  

  const navigate = useNavigate()

  const bicepsHandler = () => {

    setExercise("bicepsExersice")
  }


  const pushupsHandler = () => {

    setExercise("pushupsExersice")
  }

  const shoulderHandler = () => {

    setExercise("shoulderExersice")
  }

  const submitExercise = () => {

    console.log(Exercise)

    if (Exercise === "bicepsExersice"){
      navigate('/video')

    }
    if (Exercise === "pushupsExersice"){
      navigate('/video1')

    }
    if (Exercise === "shoulderExersice"){
      navigate('/video2')

    }
  }

  return (
    <Container>
      <div className="wrapper">
        <h3 className="head">Which excercise would you like to do today?</h3>
      </div>

      <div className="wrapper2">
        <Row>
          <Col>
            <Card style={{ width: "18rem" }} onMouseOver={bicepsHandler}>
              <Card.Img variant="top" className="image-icon" src={biceps} />
              <Card.Body>
                <Card.Title>Biceps Curl</Card.Title>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card style={{ width: "18rem" }} onMouseOver={pushupsHandler}>
              <Card.Img variant="top" className="image-icon" src={pushUp} />
              <Card.Body>
                <Card.Title>Push Ups</Card.Title>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card style={{ width: "18rem" }} onMouseOver={shoulderHandler}>
              <Card.Img variant="top" className="image-icon" src={Shoulder} />
              <Card.Body>
                <Card.Title>Shoulder Press</Card.Title>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </div>
      <div className="wrapper3">
        <Button variant="primary" onClick={submitExercise}>Confirm</Button>
      </div>
    </Container>
  );
};

export default Home;
