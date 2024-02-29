import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <div>
      Not found, go <Link to={ '/' }>back.</Link>
    </div>
  );
};

export default NotFound;