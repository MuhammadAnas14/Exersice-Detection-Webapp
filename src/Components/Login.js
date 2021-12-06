import React from 'react'
import bImage from './Assets/backImage.png'
import {Image} from 'react-bootstrap'
import './CSS/login.css'


const Login = () => {

    return(

     <div className = "login-screen">
         <Image className = "bg" src={bImage} fluid />


     </div>
    )
}

export default Login