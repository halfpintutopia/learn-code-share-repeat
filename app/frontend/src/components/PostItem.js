import React from 'react';
import css from "./css/Content.module.css";

const PostItem = (props) => {
  return (
      props.posts.map((post) => {
        const {title, name, image, description} = post
        return (
          <div key={title} className={css.SearchItem}>
            <p>{title}</p>
            <p>{name}</p>
            <img src={image} alt={title}/>
            <p>{description}</p>
          </div>
        );
      })
  );
};

export default PostItem;