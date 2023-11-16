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
      isLoaded: false
    }
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({
        isLoaded: true
      })
    }, 2000)
  }

  render() {
    return (
      <div className={css.Content}>

        <div className={css.TitleBar}>
          <h1>My Photos</h1>
        </div>
        <div className={css.SearchResults}>
          {
            this.state.isLoaded ?
              (<PostItem posts={savedPosts} />) : (<Loader />)
          }

        </div>
        Thanks for another productive morning! Have a beautiful autumnal day!
      </div>
    );
  }
}

export default Content;