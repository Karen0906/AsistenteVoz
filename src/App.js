import MainLayout from './Components/MainLayout';
import LoginScreen from './Screens/LoginScreen';
import React from 'react';
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <div>
      <AuthProvider>
      <LoginScreen/>
      </AuthProvider>
      
    </div>
  );
}

export default App;
