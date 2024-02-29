import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCloudArrowUp } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const UploadPage = () => {
  const [ file, setFile ] = useState();
  const navigate = useNavigate();

  const handleFileInput = (event) => {
    setFile(event.target.files[0]);
  };

  useEffect(() => {
    if (file) {
      navigate('/upload/manage', { state: { file } });
    }
  }, [ file, navigate ]);

  return (
    <section className="container upload-container" data-width="wide">
      <FontAwesomeIcon icon={ faCloudArrowUp }/>
      <h1 className="upload center">Choose video to upload</h1>
      <label className="btn green center" htmlFor="video">
        Choose file
      </label>
      <input id="video" type="file" onChange={ handleFileInput }/>
    </section>
  );
};

export default UploadPage;