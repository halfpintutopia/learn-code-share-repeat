import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowUpFromBracket } from "@fortawesome/free-solid-svg-icons";

const MultiInput = () => {
  const handleAddRow = () => {
  };

  return (
    <>
      <div className="form-group">
        <label htmlFor="language">Language</label>
        <input
          id="language"
          name="language"
          type="text"
          placeholder="JavaScript"
        />
        <label htmlFor="version">Version</label>
        <input
          id="version"
          name="version"
          type="text"
          placeholder="ES6"
        />
        <button>
          <FontAwesomeIcon icon={ faArrowUpFromBracket }/>
        </button>
      </div>
      <button className="btn green" onClick={ handleAddRow }>Add technologies</button>
    </>
  );
};

export default MultiInput;