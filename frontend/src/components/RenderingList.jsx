import React from "react";

import Book from "./Book";

const RenderingList = () => {
  const bookList = [
    {
      title: "To Kill a Mockingbird",
      author: "Harper Lee",
      pages: 281,
    },
    {
      title: "The Great Gatsby",
      author: "F. Scott Fitzgerald",
      pages: 218,
    },
    {
      title: "The Catcher in the Rye",
      author: "J. D. Salinger",
      pages: 234,
    },
  ];

  return (
    <div>
      {bookList.map((book, index) => {
        return <Book key={book.title} book={book} />;
      })}
    </div>
  );
};

export default RenderingList;
