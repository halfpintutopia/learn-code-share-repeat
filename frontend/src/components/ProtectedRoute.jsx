import { AuthContext } from "./AuthContext";
import { useContext } from "react";
import { Navigate } from "react-router-dom";

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useContext(AuthContext);

  if (!isAuthenticated) {
    localStorage.setItem('redirectPath', location.pathname);
    return <Navigate to="/join/login"/>;
  }
  return children;
};

export default ProtectedRoute;