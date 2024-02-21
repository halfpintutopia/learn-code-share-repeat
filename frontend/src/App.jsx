import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HelmetProvider } from 'react-helmet-async';
import "./components/sass/main.scss";
import NotFound from "./components/NotFound";
import ActivateUser from "./components/ActivateUser";
import Homepage from "./components/Homepage";
import JoinPage from "./components/JoinPage";
import { AuthProvider } from "./components/AuthContext";
import Upload from "./components/Upload";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: Infinity,
      cacheTime: Infinity,
    },
  },
});

const App = () => {
  return (
    <HelmetProvider>
      <BrowserRouter>
        <QueryClientProvider client={queryClient}>
          <AuthProvider>
            <Routes>
              <Route path="/join/:type" element={<JoinPage />} />
              <Route path="/activate/:uid/:token" element={<ActivateUser />} />
              <Route path="/" element={<Homepage />} />
              <Route path="/upload" element={<Upload />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </AuthProvider>
        </QueryClientProvider>
      </BrowserRouter>
    </HelmetProvider>
  );
};

export default App;
