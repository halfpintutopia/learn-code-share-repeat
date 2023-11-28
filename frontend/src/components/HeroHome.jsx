import React from 'react';
import css from "./css/HeroHome.module.css";
import HeaderImage from "../../public/media/videos/person_walking_on_laptop.webm";

const HeroHome = () => {
  return (
    <div className={css.HeroHome}>
      <div>
        <p>This is an overlay</p>
      </div>
      <video className={css['video-bg']} autoPlay muted loop>
        <source src={HeaderImage} type="video/webm"/>
      </video>

    </div>
  );
};

export default HeroHome;