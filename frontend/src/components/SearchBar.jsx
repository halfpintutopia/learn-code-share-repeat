import React, { Component } from "react";

import names from "../names";

class SearchBar extends Component {
  constructor(props) {
    super(props);

    this.searchBarPlaceholder = "Search names...";

    this.state = {
      searchBar: "",
      names: names,
    };
  }

  debounce = (func, delay) => {
    let debounceTimer;
    return function () {
      const context = this;
      const args = arguments;
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => func.apply(context, args), delay);
    };
  };

  handleChange = (event) => {
    const { name, value } = event.target;
    let inputText, filteredNames;
    // console.log(name, value);
    this.setState({
      [name]: value.toLowerCase(),
    });

    inputText = this.state.searchBar;

    // filteredName = this.state.names.filter((name) => name.toLowerCase().indexOf(inputText) > -1)
    filteredNames = this.state.names.filter((name) =>
      name.toLowerCase().includes(inputText),
    );

    this.setState({
      names: filteredNames,
    });

    // console.log(this.state.names);
  };

  handleSubmit = (event) => {
    event.preventDefault();
    // console.log(this.state.searchBar);
  };

  render() {
    return (
      <div>
        <h1>Name Search</h1>
        <p>matching names found: {this.state.names.length}</p>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="searchBar">
            <input
              id="searchBar"
              type="text"
              name="searchBar"
              placeholder={this.searchBarPlaceholder}
              value={this.state.searchBar}
              onChange={this.handleChange}
            />
          </label>
        </form>
        <div>We will render names here</div>
        {this.state.names.map((name, index) => {
          return <p key={name}>{name}</p>;
        })}
      </div>
    );
  }
}

export default SearchBar;
