import React from "react";

const Book = (props) => {
  return (
    <div>
      <h5>{props.book.title}</h5>
      <p>{props.book.author}</p>
      <p>{props.book.pages}</p>
    </div>
  );
};

export default Book;
