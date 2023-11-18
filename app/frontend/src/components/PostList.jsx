import React from "react";
import { useQuery } from "@tanstack/react-query";
import fetchPosts from "./fetchPosts";

const PostList = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["posts"],
    queryFn: fetchPosts,
  });

  if (isLoading) return <div>Loading</div>;

  if (isError) return <div>Error fetching posts</div>;
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
