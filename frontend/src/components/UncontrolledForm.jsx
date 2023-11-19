import React, { Component } from "react";

class ControlledForm extends Component {
  constructor(props) {
    super(props);

    this.defaultValueFullName = "John Smith";
    this.inputFullName = React.createRef();
    this.selectCategory = React.createRef();
    this.textareaComments = React.createRef();
  }

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(
      this.inputFullName.current.value,
      this.selectCategory.current.value,
      this.textareaComments.current.value,
    );
  };

  render() {
    return (
      <div>
        <h2>Please fill out the form below:</h2>
        <form onSubmit={this.handleSubmit}>
          <fieldset>
            <label htmlFor="fullName">Your Name:</label>
            <input
              name="fullName"
              id="fullName"
              type="text"
              defaultValue={this.defaultValueFullName}
              ref={this.inputFullName}
            />
          </fieldset>
          <fieldset>
            <label htmlFor="category">Category</label>
            <select name="category" id="category" ref={this.selectCategory}>
              <option value="webiste">Website issue</option>
              <option value="order">Order issue</option>
              <option value="general">General inquiry</option>
            </select>
          </fieldset>
          <fieldset>
            <label htmlFor="comments">Comments</label>
            <textarea
              name="comments"
              id="comments"
              cols="30"
              rows="10"
              ref={this.textareaComments}
            />
          </fieldset>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default ControlledForm;
