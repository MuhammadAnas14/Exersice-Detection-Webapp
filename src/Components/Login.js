import React from "react";
import bImage from "./Assets/backImage.png";
import { Image, Container  ,Button} from "react-bootstrap";
import "./CSS/login.css";

const Login = () => {
  return (
    <div className="login-screen">
      <Container>
          
        <div className="outer">
          <div className="inner">
              <h3 className="head">Login</h3>
            <form>
              <div className="form-group">
                <div className="textOnInput">
                  <label for="inputText">Email</label>
                  <input className="form-control" type="text" />
                </div>
              </div>
              <div class="form-group">
                <div class="textOnInput">
                  <label for="inputText">Password</label>
                  <input class="form-control" type="text" />
                </div>
              </div>
              <div>
              <Button variant="primary">Log In</Button>
              </div>
            </form>
          </div>
        </div>
      </Container>
    </div>
  );
};

export default Login;
