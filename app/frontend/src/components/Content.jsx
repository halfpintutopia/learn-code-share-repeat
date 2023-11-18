import React, { useEffect, useState } from "react";

import PostItem from "./PostItem";

import css from "./css/Content.module.css";
import Loader from "./Loader";
import { fetchData } from "./fetchPosts";
import { useQuery } from "@tanstack/react-query";
import API_KEY from "../../secret";

const Content = () => {
  const [posts, setPosts] = useState([]);
  const [searchValue, setSearchValue] = useState("");

  const URL = `https://pixabay.com/api/?key=${API_KEY}&q=${encodeURIComponent(
    "red roses",
  )}`;

  const useImages = () =>
    useQuery({
      queryKey: ["images"],
      queryFn: () => fetchData(URL),
    });

  const { data, isLoading, isError, error, refetch } = useImages();

  useEffect(() => {
    if (data) {
      setPosts(data.hits);
    }
  }, [data]);

  if (isLoading) return <Loader />;

  if (isError)
    return (
      <div>
        Error fetching images:{" "}
        {error instanceof Error ? error.message : String(error)}
        <button onClick={() => refetch()}>Retry</button>
      </div>
    );

  const handleChange = (event) => {
    let filteredPosts;

    const { value } = event.target;

    setSearchValue(value);

    filteredPosts = posts.filter((post) =>
      post.tags.toLowerCase().includes(value),
    );

    setPosts(filteredPosts);
  };

  return (
    <div className={css.Content}>
      <div className={css.TitleBar}>
        <h1>My Photos</h1>
        <form>
          <label htmlFor="searchInput">Search by tag:</label>
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
        <PostItem images={posts} />
      </div>
    </div>
  );
};

export default Content;
