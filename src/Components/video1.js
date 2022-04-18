import React from "react";
import {Container, Button,Image } from "react-bootstrap";
import "./CSS/video.css";



const Video = () => {
  return (
    <div className="video-screen">
      {/* <video className='videoTag' autoPlay loop>
    <source src={sample} type='video/mp4' />
      </video> */}
      <Image src="http://192.168.0.113:5050/pushupsFeeds" alt="Video" fluid />
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
