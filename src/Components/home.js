import React, { useState } from "react";
import "./CSS/home.css";
import { Container, Card, Row, Col, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import pushUp from "./Assets/push-up.png";
import biceps from "./Assets/biceps.png";
import Shoulder from "./Assets/shoulder.png";

const Home = () => {
  const [Exercise, setExercise] = useState("");
  const [isActive, setActive] = useState(null);

  const [ExerciseItem, setExerciseItem] = useState([
    { id: 1, name: "Biceps Curl", to: biceps, className: "card" },
    { id: 2, name: "Push Ups", to: pushUp, className: "card" },
    { id: 3, name: "Shoulder Press", to: biceps, className: "card" },
  ]);

  const navigate = useNavigate();


  const confirmExercise = () => {

    if (isActive === 1){
      setExercise("bicepsExersice");
    }
    if (isActive === 2){
      setExercise("pushupsExersice");
    }
    if (isActive === 3){
      setExercise("shoulderExersice");
    }
  };

  const submitExercise = () => {
    console.log(Exercise);

    if (Exercise === "bicepsExersice") {
      navigate("/video");
    }
    if (Exercise === "pushupsExersice") {
      navigate("/video1");
    }
    if (Exercise === "shoulderExersice") {
      navigate("/video2");
    }
  };

  const toggleHandle =(id)=>{
    setActive(id)
    console.log(id)

  }

  return (
    <Container>
      <div className="wrapper">
        <h3 className="head">Which excercise would you like to do today?</h3>
      </div>

      <div className="wrapper2">
        <Row>
          {ExerciseItem.map((item) => {
            return (
              <Col>
                <Card style={{ width: "18rem" }} className={item.className +(item.id === isActive ? " card1" : "")} onMouseOver={confirmExercise} onClick={()=>toggleHandle(item.id)}>
                  <Card.Img
                    variant="top"
                    className="image-icon"
                    src={item.to}
                  />
                  <Card.Body>
                    <Card.Title>{item.name}</Card.Title>
                  </Card.Body>
                </Card>
              </Col>
            );
          })}
        </Row>
      </div>
      <div className="wrapper3">
        <Button variant="primary" onClick={submitExercise}>
          Confirm
        </Button>
      </div>
    </Container>
  );
};

export default Home;
