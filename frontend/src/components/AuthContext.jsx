import { createContext, useState, useEffect } from "react";

// Returns an object with 2 React components: Provider and Consumer
const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [ isAuthenticated, setIsAuthenticated ] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('access_token');

    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  return (
    <AuthContext.Provider value={ { isAuthenticated, setIsAuthenticated } }>
      { children }
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };