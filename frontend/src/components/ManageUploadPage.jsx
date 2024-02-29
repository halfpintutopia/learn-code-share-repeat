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
        <div className="btn-group">
          <button className="btn btn__delete">
            Delete
          </button>
          <button className="btn btn__unpublish">
            Unpublish
          </button>
        </div>
        <video className="video-bg" muted>
          <source src={ fileUrl } type="video/webm"/>
        </video>

        <form>
          <div className="form-group">
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
          </div>
          <div className="form-group">
            <MultiInput/>
          </div>
        </form>
      </div>
      <Footer/>
    </>
  );
};

export default ManageUploadPage;