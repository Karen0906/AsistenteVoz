import MainLayout from './Components/MainLayout';
import LoginScreen from './Screens/LoginScreen';
import React from 'react';
import { AuthProvider } from "./context/AuthContext";
import Profile from './Screens/Profile';
import SignupScreen from './Screens/SignupScreen';

function App() {
  return (
    <div>
      <AuthProvider>
      <LoginScreen/> 
      
      <MainLayout/>
      <Profile/>
      </AuthProvider>
    </div>
  );
}

export default App;
