import React from 'react';
import Demo from "../../public/media/images/computer_program.jpg";
import { faChevronLeft, faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const HeroCarousel = () => {
  // const [ currentSlide, setCurrentSlide ] = useState(false);


  return (
    <section>
      <div className="carousel">
        <button className="carousel__button carousel__button--left">
          <FontAwesomeIcon icon={ faChevronLeft }/>
        </button>
        <div className="carousel__track-container">
          <ul className="carousel__track">
            {/*TODO loop videos*/ }
            <li className="carousel__slide">
              <img className="carousel__image" src={ Demo } alt="a test"/>
              {/*<div className="carousel__slide--item">*/ }
              {/*  <div className="item__overlay">*/ }
              {/*    <h1 className="item__title">Code with Clarity & Confidence</h1>*/ }
              {/*  </div>*/ }
              {/*  <video className="item__background-media" autoPlay muted loop>*/ }
              {/*    <source src={HeaderImage} type="video/webm" />*/ }
              {/*  </video>*/ }
              {/*</div>*/ }
            </li>
          </ul>
        </div>
        <button className="carousel__button carousel__button--right">
          <FontAwesomeIcon icon={ faChevronRight }/>
        </button>

        <div className="carousel__nav">
          {/*TODO loop number of videos*/ }
          {/*<button className="carousel__indicator" data-slide={ currentSlide }></button>*/}
        </div>
      </div>
    </section>
  );
};

export default HeroCarousel;