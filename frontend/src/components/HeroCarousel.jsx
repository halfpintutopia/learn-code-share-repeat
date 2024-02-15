import { faChevronLeft, faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useState } from "react";

const HeroCarousel = ({ slides }) => {
  const [ currentSlide, setCurrentSlide ] = useState(0);
  const navigateSlide = (direction) => {
    if (direction === 'next') {
      setCurrentSlide(currentSlide === slides.length - 1 ? 0 : currentSlide + 1);
    } else {
      setCurrentSlide(currentSlide === 0 ? slides.length - 1 : currentSlide - 1);
    }
  };
  return (
    <>
      <section className="carousel" aria-label="Newest Photos">
        <div className="container" data-width="wide">
          <button
            className="carousel__button prev"
            data-carousel-btn="prev"
            onClick={ () => navigateSlide('prev') }
          >
            <FontAwesomeIcon icon={ faChevronLeft }/>
          </button>
          <button
            className="carousel__button next"
            data-carousel-btn="next"
            onClick={ () => navigateSlide('next') }
          >
            <FontAwesomeIcon icon={ faChevronRight }/>
          </button>
        </div>
        <div className="carousel__wrapper">
          <ul>
            {
              [ ...slides ].map((slide, index) => (
                <>
                  <li
                    key={ index }
                    className="carousel__slide"
                    data-current-slide={ currentSlide === index ? 'true' : 'false' }
                  >
                    {
                      slide.mediaType === 'img' ? (
                        <img src={ slide.mediaSrc } alt={ slide.altTag }/>
                      ) : slide.mediaType === 'video' ? (
                        // eslint-disable-next-line jsx-a11y/media-has-caption
                        <video src={ slide.mediaSrc }></video>
                      ) : null
                    }
                  </li>
                  <div className="overlay">
                    <div className="container" data-width="wide">Hello</div>
                  </div>
                </>
              ))
            }
          </ul>
        </div>
      </section>
    </>
  )
    ;
};

export default HeroCarousel;