import React from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function LoginScreen() {
  const [user, setUser] = useState({
    email: "",
    password: "",
  });
  const { login, loginWithGoogle, resetPassword } = useAuth();
  const [error, setError] = useState("");
  
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      await login(user.email, user.password);
      navigate("/");
    } catch (error) {
      setError(error.message);
    }
  };

  const handleChange = ({ target: { value, name } }) =>
    setUser({ ...user, [name]: value });

  const handleGoogleSignin = async () => {
    try {
      await loginWithGoogle();
      navigate("/");
    } catch (error) {
      setError(error.message);
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    if (!user.email) return setError("Write an email to reset password");
    try {
      await resetPassword(user.email);
      setError('We sent you an email. Check your inbox')
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div class= 'mt-5'>
    <div class="row justify-content-md-center align-items-center ">
    <Card border = "white" style={{ width: '23%' }}>
      <Card.Body className='text-center'>
        <Card.Title className='fw-bold fs-1'>Log in</Card.Title>
        <Card.Text className='fw-normal text-secondary'>
          Inicia sesión con la cuenta de tu empresa para acceder al algoritmo.
        </Card.Text>
        <Form>
      <Form.Group className="mb-4" controlId="formBasicEmail">
        <Form.Control type="email" placeholder="Email" name="email"
            id="email"
            onChange={handleChange}/>
      </Form.Group>

      <Form.Group className="mb-4" controlId="formBasicPassword">
        <Form.Control type="password" placeholder="Password" name="password"
            id="password"
            onChange={handleChange}/>
      </Form.Group>
      <Button variant="primary" type="submit" style={{ width: '70%' ,  backgroundColor:'#d40078',  borderColor:'#d40078'}} onSubmit={handleSubmit}>
        Login
      </Button>
      <div class="w-100, mt-3">
      <a
            className="inline-block align-baseline font-bold text-sm "
            href="#!"
            style = "color:#d40078"
            onClick={handleResetPassword}
          >
            Forgot your Password?
          </a>
          </div>
    </Form>
      </Card.Body>
    </Card>
    </div>
    </div>

  )
}

export default LoginScreen;

