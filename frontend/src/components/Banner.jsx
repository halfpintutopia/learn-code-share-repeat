import React from 'react';
import './sass/main.scss';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCode, faLaptopFile, faRepeat, faShareNodes} from "@fortawesome/free-solid-svg-icons";

const Banner = (props) => {
  return (
    <section className="banner container grid grid-columns" data-width="wide" data-columns={props.columns}>
      <div>
        <FontAwesomeIcon icon={faLaptopFile} />
        <h2 className="landing">Learn</h2>
        <p>Choose a language, framework, technology. Find a book or a platform and learn.</p>
      </div>
      <div>
        <FontAwesomeIcon icon={faCode} />
        <h2 className="landing">Code</h2>
        <p>Put into practice what you have learnt. Prepare a sample.</p>
      </div>
      <div>
        <FontAwesomeIcon icon={faShareNodes} />
        <h2 className="landing">Share</h2>
        <p>Create a video with the code sample and share your knowledge.</p>
      </div>
      <div>
        <FontAwesomeIcon icon={faRepeat} />
        <h2 className="landing">Repeat</h2>
        <p>Get feedback, learn to assess yourself and improve.</p>
      </div>
    </section>
  );
};

export default Banner;