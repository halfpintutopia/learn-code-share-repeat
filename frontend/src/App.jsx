import React from "react";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {BrowserRouter, Routes, Route} from "react-router-dom";
import "./components/sass/app.scss";
import HeroHome from "./components/HeroHome";
import Header from "./components/Header";
import NotFound from "./components/NotFound";

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
        <Header/>
        <HeroHome/>

        <Routes>
          {/*<Route path="/details/:id" element={<Details />} />*/}
          {/*<Route path="/" element={<SearchParams />} />*/}
          {/*<Route path="/" element={<Homepage/>}/>*/}
          <Route path="*" element={
            <NotFound/>
          } />
        </Routes>
      </QueryClientProvider>
    </BrowserRouter>
  );
};

export default App;
