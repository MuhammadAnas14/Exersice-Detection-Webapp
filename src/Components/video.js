import React from "react";
import { Image, Container, Button } from "react-bootstrap";
import "./CSS/video.css";

const Video = () => {
  return (
    <div className="video-screen">
      <Container>
        <div className="wrapper">
          <h3 className="head1">Web cam is started</h3>
        </div>
        <div className="btn-pos">
          <Button variant="primary">Stop</Button>
        </div>

      </Container>
    </div>
  );
};

export default Video;
