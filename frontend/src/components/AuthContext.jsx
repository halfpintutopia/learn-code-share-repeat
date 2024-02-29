import { createContext, useState, useEffect } from "react";

// Returns an object with 2 React components: Provider and Consumer
const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [ isAuthenticated, setIsAuthenticated ] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('access_token');

    if (!token) {
      setIsAuthenticated(false);
    } else {
      setIsAuthenticated(true);
    }
  }, []);

  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={ { isAuthenticated, setIsAuthenticated, logout } }>
      { children }
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };