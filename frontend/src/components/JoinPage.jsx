import React from 'react';
import './sass/main.scss';
// import JoinImage from "../../public/media/videos/digital_presentation_on_screen.webm";
import JoinImage from "../media/videos/digital_presentation_on_screen.webm";
import AccessibleTabs from "./AccessibleTabs";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import HeaderSimple from "./HeaderSimple";
import { useParams } from "react-router-dom";
import Footer from "./Footer";

const JoinPage = () => {
  const { type } = useParams();
  const tabs = [
    {
      id: 'login',
      title: 'Login',
      content: <LoginForm/>
    },
    {
      id: 'register',
      title: 'Register',
      content: <RegisterForm/>
    }
  ];

  return (
    <>
      <HeaderSimple/>
      <main className="join-container stacked-grid forms">
        <video className="background-media" autoPlay muted loop>
          <source src={ JoinImage } type="video/webm"/>
        </video>
        <div className="container" data-width="narrow">
          <AccessibleTabs tabs={ tabs } type={ type }/>
        </div>
      </main>
      <Footer/>
    </>
  );
};

export default JoinPage;