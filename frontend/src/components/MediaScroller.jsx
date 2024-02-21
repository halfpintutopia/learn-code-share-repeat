import { Link } from "react-router-dom";
import { getAllVideos } from "../utils/video";
import { useEffect, useState } from "react";

const MediaScroller = () => {
  const [videos, setVideos] = useState([]);

  // useEffect(() => {
  //   const fetchVideos = async () => {
  //     const videos = await getAllVideos();
  //     console.log(11,  videos);
  //     // setVideos(videos);
  //   }
  //
  //   fetchVideos();
  // }, []);


  return (
    <>
      <section className="horizontal-media-scroller">
        <article className="horizontal-media-scroller__wrapper">
          <ul className="horizontal-media-scroller__list" tabIndex="-1">
            {/*{*/}
            {/*  [...videos].map((video) => (*/}
            {/*    <li>*/}
            {/*      <Link to={ video.link } tabIndex="0">*/}
            {/*        <figure>*/}
            {/*          <picture>*/}
            {/*            <img alt={ video.title } loading="lazy" src={ video.image }/>*/}
            {/*          </picture>*/}
            {/*          <figcaption>{ video.user } | {video.technology_used}</figcaption>*/}
            {/*        </figure>*/}
            {/*      </Link>*/}
            {/*    </li>*/}
            {/*  ))*/}
            {/*}*/}
            <li key="1">
              <Link to="#" tabIndex="0">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?14"/>
                  </picture>
                  <figcaption>The Strain (limited)</figcaption>
                </figure>
              </Link>
            </li>
            <li key="2">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?15"/>
                  </picture>
                  <figcaption>The Following</figcaption>
                </figure>
              </Link>
            </li>
            <li key="3">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?16"/>
                  </picture>
                  <figcaption>BERLIN STATION</figcaption>
                </figure>
              </Link>
            </li>
            <li key="4">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?17"/>
                  </picture>
                  <figcaption>Penny Dreadful</figcaption>
                </figure>
              </Link>
            </li>
            <li key="5">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?18"/>
                  </picture>
                  <figcaption>Castle Rock</figcaption>
                </figure>
              </Link>
            </li>
            <li key="6">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?19"/>
                  </picture>
                  <figcaption>The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
            <li key="7">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?11"/>
                  </picture>
                  <figcaption>Legends</figcaption>
                </figure>
              </Link>
            </li>
            <li key="8">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?12"/>
                  </picture>
                  <figcaption>The Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="9">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?13"/>
                  </picture>
                  <figcaption>Almost Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="10">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?110"/>
                  </picture>
                  <figcaption>Fear The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
            <li key="11">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?121"/>
                  </picture>
                  <figcaption>Legends</figcaption>
                </figure>
              </Link>
            </li>
            <li key="12">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?132"/>
                  </picture>
                  <figcaption>The Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="13">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?123"/>
                  </picture>
                  <figcaption>Almost Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="14">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?144"/>
                  </picture>
                  <figcaption>The Strain</figcaption>
                </figure>
              </Link>
            </li>
            <li key="15">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?125"/>
                  </picture>
                  <figcaption>The Following</figcaption>
                </figure>
              </Link>
            </li>
            <li key="16">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?126"/>
                  </picture>
                  <figcaption>BERLIN STATION</figcaption>
                </figure>
              </Link>
            </li>
            <li key="17">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?137"/>
                  </picture>
                  <figcaption>Penny Dreadful</figcaption>
                </figure>
              </Link>
            </li>
            <li key="18">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?118"/>
                  </picture>
                  <figcaption>Castle Rock</figcaption>
                </figure>
              </Link>
            </li>
            <li key="19">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?419"/>
                  </picture>
                  <figcaption>The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
            <li key="20">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?110"/>
                  </picture>
                  <figcaption>Fear The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
            <li key="21">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?112"/>
                  </picture>
                  <figcaption>Legends</figcaption>
                </figure>
              </Link>
            </li>
            <li key="22">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?122"/>
                  </picture>
                  <figcaption>The Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="23">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?313"/>
                  </picture>
                  <figcaption>Almost Family</figcaption>
                </figure>
              </Link>
            </li>
            <li key="24">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?194"/>
                  </picture>
                  <figcaption>The Strain</figcaption>
                </figure>
              </Link>
            </li>
            <li key="25">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?915"/>
                  </picture>
                  <figcaption>The Following</figcaption>
                </figure>
              </Link>
            </li>
            <li key="26">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?176"/>
                  </picture>
                  <figcaption>BERLIN STATION</figcaption>
                </figure>
              </Link>
            </li>
            <li key="27">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?187"/>
                  </picture>
                  <figcaption>Penny Dreadful</figcaption>
                </figure>
              </Link>
            </li>
            <li key="28">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?178"/>
                  </picture>
                  <figcaption>Castle Rock</figcaption>
                </figure>
              </Link>
            </li>
            <li key="29">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?189"/>
                  </picture>
                  <figcaption>The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
            <li key="30">
              <Link to="#" tabIndex="-1">
                <figure>
                  <picture>
                    <img alt="A placeholder image" loading="lazy" src="https://picsum.photos/500/500?117"/>
                  </picture>
                  <figcaption>Fear The Walking Dead</figcaption>
                </figure>
              </Link>
            </li>
          </ul>
        </article>
      </section>
    </>
  );
};

export default MediaScroller;