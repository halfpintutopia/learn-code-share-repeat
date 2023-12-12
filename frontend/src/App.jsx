import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./components/sass/app.scss";
import NotFound from "./components/NotFound";
import ActivateUser from "./components/ActivateUser";
import Homepage from "./components/Homepage";
import JoinPage from "./components/JoinPage";

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
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <Routes>
          <Route path="/join/:type" element={<JoinPage />} />
          <Route path="/activate/:uid/:token" element={<ActivateUser />} />
          <Route path="/" element={<Homepage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </QueryClientProvider>
    </BrowserRouter>
  );
};

export default App;
