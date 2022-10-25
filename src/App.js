import MainLayout from './Components/MainLayout';
import React from 'react';
import Profile from './Screens/Profile';
import SignupScreen from './Screens/SignupScreen';

function App() {
  return (
    <div>
      <MainLayout/>
      <Profile/>
      <SignupScreen></SignupScreen>
    </div>
  );
}

export default App;
