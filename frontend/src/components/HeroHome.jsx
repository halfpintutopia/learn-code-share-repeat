import React from 'react';
import HeaderImage from "../../public/media/videos/person_walking_on_laptop.webm";
import './sass/app.scss';

const HeroHome = () => {
  return (
    <div className="video-container container" data-width="wide">
      <div className="overlay">
        <h1 className="title">Code with Clarity & Confidence</h1>
      </div>
      <video className="video-bg" autoPlay muted loop>
        <source src={HeaderImage} type="video/webm"/>
      </video>

    </div>
  );
};

export default HeroHome;