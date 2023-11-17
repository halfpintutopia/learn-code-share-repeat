import React, {Component} from 'react';

import PostItem from "./PostItem";

import css from "./css/Content.module.css";
import data from "../posts.json";
import Loader from "./Loader";

const {savedPosts} = data

class Content extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoaded: false,
      posts: [],
      searchValue: ''
    }
  }

  handleChange = event => {
    let filteredPosts

    const {value} = event.target

    this.setState({
      searchValue: value
    })

    filteredPosts = this.state.posts.filter((post) => post.name.toLowerCase().includes(this.state.searchValue))

    this.setState({
      posts: filteredPosts
    })
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({
        isLoaded: true,
        posts: savedPosts
      })
    }, 1000)
  }

  render() {
    return (
      <div className={css.Content}>

        <div className={css.TitleBar}>
          <h1>My Photos</h1>
          <form>
            <label htmlFor="searchInput">Search:</label>
            <input
              id="searchInput"
              type="search"
              onChange={this.handleChange}
              value={this.state.searchValue}
            />
            <h4>posts found: {this.state.posts.length}</h4>
          </form>
        </div>
        <div className={css.SearchResults}>
          {
            this.state.isLoaded ?
              (<PostItem posts={this.state.posts} />) : (<Loader />)
          }

        </div>
        Thanks for another productive morning! Have a beautiful autumnal day!
      </div>
    );
  }
}

export default Content;