import React from "react";
import { Container  ,Button} from "react-bootstrap";
import {Link } from "react-router-dom";
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
              <div className="btn-pos">
              <Link to="/main"><Button variant="primary">Log In</Button></Link>
              </div>
            </form>
          </div>
        </div>
      </Container>
    </div>
  );
};

export default Login;
