import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCloudArrowUp } from "@fortawesome/free-solid-svg-icons";

const UploadPage = () => {
  return (
    <section className="container upload-container" data-width="wide">
      <FontAwesomeIcon icon={ faCloudArrowUp }/>
      <h1 className="upload center">Choose video to upload</h1>
      <button className="btn green">Choose file</button>
    </section>
  );
};

export default UploadPage;