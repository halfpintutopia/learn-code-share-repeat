import React from "react";
import { useQuery } from "@tanstack/react-query";
import { fetchData } from "./fetchPosts";

const PostList = () => {
  const usePosts = () =>
    useQuery({
      queryKey: ["posts"],
      queryFn: fetchData,
    });

  const { data, isLoading, isError, error, refetch } = usePosts();

  if (isLoading) return <div>Loading</div>;

  if (isError)
    return (
      <div>
        Error fetching posts: {error instanceof Error ? error.message : String(error)}
        <button onClick={() => refetch()}>Retry</button>
      </div>
    );
  return (
    <div>
      {data.map((post) => (
        <div key={post.id}>
          <h2>
            {post.id}. {post.title}
          </h2>
          <h4>By User ID {post.userId}</h4>
          <p>{post.body}</p>
          <hr />
        </div>
      ))}
    </div>
  );
};

export default PostList;
