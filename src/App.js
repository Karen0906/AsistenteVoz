import MainLayout from './Components/MainLayout';
import React from 'react';
import Profile from './Screens/Profile';
import HomeScreen from './Screens/HomeScreen';


function App() {
  return (
    <div>
      <MainLayout/>
      <HomeScreen/>
      {/* <Profile/> */}
    </div>
  );
}

export default App;
