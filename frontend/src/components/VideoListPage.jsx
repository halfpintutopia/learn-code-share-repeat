import HeroCarousel from "./HeroCarousel";

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
    <main>
      <HeroCarousel slides={ slides }/>
      Video List Page
    </main>
  );
};

export default VideoListPage;