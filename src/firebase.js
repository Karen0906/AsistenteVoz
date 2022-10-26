// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from 'firebase/auth';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD9mCcir9500GHRFJUiVwqKVg8-OFfdSpw",
  authDomain: "asistente-voz-bb06c.firebaseapp.com",
  projectId: "asistente-voz-bb06c",
  storageBucket: "asistente-voz-bb06c.appspot.com",
  messagingSenderId: "1050065426840",
  appId: "1:1050065426840:web:98937107a413f160ae73ed"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);

//Authentication
export const auth = getAuth(app);