import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import css from "./App.module.css";
// import NavBarSimple from "./components/NavBarSimple";
import Homepage from "./components/Homepage";
import PostList from "./components/PostList";

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
        <div className={css.App}>
          <header className="App-header">
            {/*<NavBarSimple />*/}
          </header>
          <PostList />
          <Routes>
            {/*<Route path="/details/:id" element={<Details />} />*/}
            {/*<Route path="/" element={<SearchParams />} />*/}
            <Route path="/" element={<Homepage />} />
          </Routes>
        </div>
      </QueryClientProvider>
    </BrowserRouter>
  );
};

export default App;
