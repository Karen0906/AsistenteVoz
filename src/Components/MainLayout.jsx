import React, { Fragment } from 'react';
import logo from '../Assets/logo.svg';

function App() {
  return (
    <div>
      <header>
        <nav class="navbar navbar-expand-sm navbar-light bg-light">
            <div class="container-fluid">
                <img src={logo} width="100" height="60"/>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 justify-content-left">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Profile</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Login</a>
                    </li>
                  </ul>
                <form class="d-flex">

                    {/* <button class="btn btn-outline-info mx-1" type="button">Home</button>
                    <button class="btn btn-outline-info mx-1" type="button">Profile</button>
                    <button class="btn btn-outline-info mx-1" type="button">Login</button>
                    <button class="btn btn-outline-info mx-1" type="submit">Sign up</button> */}

                </form>
                </div>
            </div>
        </nav>
      </header>
    </div>
  );
}

export default App;
