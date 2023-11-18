import React, { useEffect, useState } from "react";

import PostItem from "./PostItem";

import css from "./css/Content.module.css";
import DATA from "../posts.json";
import Loader from "./Loader";

const { savedPosts } = DATA;

const Content = () => {
  const [loaded, setLoaded] = useState(false);
  const [posts, setPosts] = useState([]);
  const [searchValue, setSearchValue] = useState("");

  const handleChange = (event) => {
    let filteredPosts;

    const { value } = event.target;

    setSearchValue(value);

    filteredPosts = posts.filter((post) =>
      post.name.toLowerCase().includes(value),
    );

    setPosts(filteredPosts);
  };

  useEffect(() => {
    setTimeout(() => {
      setLoaded(true);
      setPosts(savedPosts);
    }, 1000);
  }, [loaded]);

  return (
    <div className={css.Content}>
      <div className={css.TitleBar}>
        <h1>My Photos</h1>
        <form>
          <label htmlFor="searchInput">Search:</label>
          <input
            id="searchInput"
            type="search"
            onChange={handleChange}
            value={searchValue}
          />
          <h4>posts found: {posts.length}</h4>
        </form>
      </div>
      <div className={css.SearchResults}>
        {loaded ? <PostItem posts={posts} /> : <Loader />}
      </div>
    </div>
  );
};

export default Content;
