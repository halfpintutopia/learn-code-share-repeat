import React from 'react';
import css from "./css/HeroHome.module.scss";
import HeaderImage from "../../public/media/videos/person_walking_on_laptop.webm";

const HeroHome = () => {
  return (
    <div className={css.videoContainer}>
      <div className={css.overlay}>
        <h1 className={css.title}>Code with Clarity & Confidence</h1>
      </div>
      <video className={css.videoBg} autoPlay muted loop>
        <source src={HeaderImage} type="video/webm"/>
      </video>

    </div>
  );
};

export default HeroHome;