import React, {Component} from 'react';

import PostItem from "./PostItem";

import css from "./css/Content.module.css";
import data from "../posts.json";

const {savedPosts} = data

class Content extends Component {
  constructor(props) {
    super(props);

  }

  render() {
    return (
      <div className={css.Content}>
        <div className={css.TitleBar}>
          <h1>My Photos</h1>
        </div>
        <div className={css.SearchResults}>
          <PostItem posts={savedPosts} />
        </div>

      </div>
    );
  }
}

export default Content;