import React, {useState} from 'react';

const ControlledForm = () => {
  const [fullName, setName] = useState('');
  const [category, setCategory] = useState('website');
  const [comments, setComments] = useState('');

  const handleSubmit = e => {
    e.preventDefault();
    console.log(fullName, category, comments)
  }

  // function handleChange(setter) {
  //   return function(e) {
  //     setter(e.target.value)
  //   }
  // }
  const handleChange = setter => e => setter(e.target.value)

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
            onChange={handleChange(setName)}
          />
        </fieldset>
        <fieldset>
          <label htmlFor="category">Category</label>
          <select
            name="category"
            id="category"
            value={category}
            onChange={handleChange(setCategory)}>
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
                    onChange={handleChange(setComments)}></textarea>
        </fieldset>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ControlledForm;