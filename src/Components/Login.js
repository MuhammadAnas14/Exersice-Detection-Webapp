import React ,{useState} from "react";
import { Container  ,Button} from "react-bootstrap";
import {Link ,useNavigate } from "react-router-dom";
import "./CSS/login.css";

const Login = () => {

  const [email, setemail] = useState("");
  const [password, setpassword] = useState("");


  let users = [

    {
      email:"admin@gmail.com",
      password:"admin"
    },
    {
      email: "user1@gmail.com",
      password: "user123"
    }
  ]

  let history = useNavigate();

  const loginSubmit = (event) => {
    event.preventDefault();

    let data = {
      email: email,
      password: password,
    };

    console.log(data)

    for(let i=0;i<users.length;i++){


      
      if(data.email === users[i].email && data.password === users[i].password){
        history('/main')
        break
      }
      else{
        console.log("wrong credential")
      }
    }

    

  };

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
                  <input className="form-control" type="text" onChange={(ev) => setemail(ev.target.value)} />
                </div>
              </div>
              <div class="form-group">
                <div class="textOnInput">
                  <label for="inputText">Password</label>
                  <input class="form-control" type="password" onChange={(ev) => setpassword(ev.target.value)}/>
                </div>
              </div>
              <div className="btn-pos">
              <Button variant="primary" onClick={loginSubmit}>Log In</Button>
              </div>
            </form>
          </div>
        </div>
      </Container>
    </div>
  );
};

export default Login;
