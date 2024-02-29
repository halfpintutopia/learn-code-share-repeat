import HeroCarousel from "./HeroCarousel";
import MediaScroller from "./MediaScroller";
import { Helmet } from "react-helmet-async";

const VideoListPage = () => {
  const slides = [
    {
      mediaType: 'img',
      mediaSrc: 'https://source.unsplash.com/random/?fruit',
      altTag: 'Fruit image'
    },
    {
      mediaType: 'img',
      mediaSrc: 'https://source.unsplash.com/random/?vegetable',
      altTag: 'Vegetable image'
    },
    {
      mediaType: 'img',
      mediaSrc: 'https://source.unsplash.com/random/?kitchen',
      altTag: 'Kitchen image'
    }
  ];
  return (
    <>
      <Helmet>
        <title>Video List</title>
      </Helmet>
      <main>
        <HeroCarousel slides={ slides }/>
        <MediaScroller/>
      </main>
    </>
  );
};

export default VideoListPage;