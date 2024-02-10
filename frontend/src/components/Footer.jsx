import React from 'react';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFacebook, faInstagram, faLinkedin, faTwitter} from "@fortawesome/free-brands-svg-icons";

const Footer = () => {
  return (
    <>
      <footer>
        <section className="container" data-width="wide">
          <div className="grid grid-columns" data-columns="2">
            <div className="social-links flex columns">
              <FontAwesomeIcon icon={faLinkedin}/>
              <FontAwesomeIcon icon={faFacebook}/>
              <FontAwesomeIcon icon={faInstagram}/>
              <FontAwesomeIcon icon={faTwitter}/>
            </div>
            <div>
              <small>2023 Learn Code Share Repeat</small>
            </div>
          </div>
        </section>
      </footer>
    </>
  );
};

export default Footer;