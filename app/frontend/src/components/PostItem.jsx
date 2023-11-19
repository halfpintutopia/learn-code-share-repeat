import React from "react";
import css from "./css/Content.module.css";

const PostItem = (props) => {
  return props.images.map((post, index) => {
    const { type, user, webformatURL, tags } = post;
    return (
      <div key={index} className={css.SearchItem}>
        <p>{type}</p>
        <p>{user}</p>
        <img src={webformatURL} alt={type} />
        <p>{tags}</p>
      </div>
    );
  });
};

export default PostItem;
