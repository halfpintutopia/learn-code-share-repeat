import React, {Component} from 'react';

class ControlledForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fullName: '',
      category: 'website',
      comments: ''
    }
  }

  handleChange = e => {
    const {name, value} = e.target
    console.log(name, value)
    this.setState({
      [name]: value
    })
  }

  handleSubmit = e => {
    e.preventDefault();
    console.log(this.state.fullName, this.state.category, this.state.comments)
  }

  render() {
    return (
      <div>
        <h2>Please fill out the form below:</h2>
        <form onSubmit={this.handleSubmit}>
          <fieldset>
            <label htmlFor="fullName">Your Name:</label>
            <input name="fullName" id="fullName" type="text" value={this.state.fullName} onChange={this.handleChange}/>
          </fieldset>
          <fieldset>
            <label htmlFor="category">Category</label>
            <select name="category" id="category" value={this.state.category} onChange={this.handleChange}>
              <option value="webiste">Website issue</option>
              <option value="order">Order issue</option>
              <option value="general">General inquiry</option>
            </select>
          </fieldset>
          <fieldset>
            <label htmlFor="comments">Comments</label>
            <textarea name="comments" id="comments" cols="30" rows="10" value={this.state.comments} onChange={this.handleChange}></textarea>
          </fieldset>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default ControlledForm;