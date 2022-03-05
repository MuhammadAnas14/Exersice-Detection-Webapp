import React from "react";
import {Container, Button,Image } from "react-bootstrap";
import "./CSS/video.css";
import sample from './Assets/Course_Overview.mp4'


const Video = () => {
  return (
    <div className="video-screen">
      {/* <video className='videoTag' autoPlay loop>
    <source src={sample} type='video/mp4' />
      </video> */}
      <Image src="http://192.168.236.3:5050/video_feed" alt="Video" fluid />
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
