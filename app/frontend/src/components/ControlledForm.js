import React, {useState} from 'react';

const ControlledForm = () => {
  const {fullName, setName} = useState();
  const {category, setCategory} = useState();
  const {comments, setComments} = useState();

  const handleSubmit = e => {
    e.preventDefault();
    console.log(fullName, category, comments)
  }

  return (
    <div>
      <h2>Please fill out the form below:</h2>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <label htmlFor="fullName">Your Name:</label>
          <input
            name="fullName"
            id="fullName"
            type="text" value={fullName}
            onChange={(e) => setName(e.target.value)}
          />
        </fieldset>
        <fieldset>
          <label htmlFor="category">Category</label>
          <select
            name="category"
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}>
            <option value="webiste">Website issue</option>
            <option value="order">Order issue</option>
            <option value="general">General inquiry</option>
          </select>
        </fieldset>
        <fieldset>
          <label htmlFor="comments">Comments</label>
          <textarea name="comments"
                    id="comments"
                    cols="30"
                    rows="10"
                    value={comments}
                    onChange={(e) => setComments(e.target.value)}></textarea>
        </fieldset>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ControlledForm;