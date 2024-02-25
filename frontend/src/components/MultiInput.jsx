const MultiInput = () => {
  return (
    <div className="form-group">
      <label
        htmlFor="language">
        <input
          id="language"
          name="language"
          type="text"
          placeholder="JavaScript"
        />
      </label>
      <label
        htmlFor="version">
        <input
          id="version"
          name="version"
          type="text"
          placeholder="ES6"
        />
      </label>
      <button className="btn green">Add technologies</button>
    </div>
  );
};

export default MultiInput;