import MainLayout from './Components/MainLayout';
import React from 'react';
import Profile from './Screens/Profile';
import SignupScreen from './Screens/SignupScreen';
import LoginScreen from './Screens/LoginScreen'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes
} from "react-router-dom";
import HomeScreen from './Screens/HomeScreen';

function App() {
  return (

    <div>
      <MainLayout/>
      <Router>
        <Routes>
          <Route path='/' element={<HomeScreen/>}/>
          <Route path='/profile' element={<Profile/>}/>
          <Route path='/login' element={<SignupScreen/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
