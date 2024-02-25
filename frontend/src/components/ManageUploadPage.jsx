import NavBar from "./NavBar";
import Footer from "./Footer";
import { useLocation } from "react-router-dom";
import { useState } from "react";
import MultiInput from "./MultiInput";

const ManageUploadPage = () => {
  const [ formValues, setFormValues ] = useState({
    title: '',
    description: '',
    coverImage: null
  });
  const location = useLocation();
  const file = location.state.file;

  const fileUrl = URL.createObjectURL(file);
  console.log(fileUrl);

  const handleInputChange = (e) => {
    e.preventDefault();
    const { name, value } = e.target;
    setFormValues(prevState => ({
      ...prevState, [name]: value
    }));
  };

  return (
    <>
      <NavBar/>

      <div className="container" data-width="wide">
        {/*<img src={ fileUrl } alt={ file.name }/>*/ }
        <button
          className="btn"
        >
          Delete
        </button>
        <button
          className="btn"
        >
          Unpublish
        </button>
        <video className="video-bg" muted>
          <source src={ fileUrl } type="video/webm"/>
        </video>

        <form>
          <label htmlFor="video-title">Title</label>
          <input
            type="text"
            placeholder="My quirky video"
            name="title"
            value={ formValues.title }
            onChange={ handleInputChange }
          />

          <label htmlFor="video-description">Description</label>
          <textarea
            onChange={ handleInputChange }
            value={ formValues.description }
            name="description"
            id="video-description"
            cols="30"
            rows="10"></textarea>

          <label htmlFor="video-cover-image">Cover image</label>
          <input id="video-cover-image" name="cover-image" type="file"/>

          <MultiInput/>
        </form>
      </div>

      <Footer/>
    </>
  );
};

export default ManageUploadPage;