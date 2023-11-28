import React from "react";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import { BrowserRouter, Routes} from "react-router-dom";
import HeroHome from "./components/HeroHome";

// import NavBarSimple from "./components/NavBarSimple";
import Header from "./components/Header";

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
        {/*<div className={css.App}>*/}
        {/*  <header className="App-header">*/}
        {/*    /!*<NavBarSimple/>*!/*/}
        {/*    <Link to="/users">Register</Link>*/}
        {/*  </header>*/}
        <Header/>
        <HeroHome/>
        <Routes>
          {/*<Route path="/details/:id" element={<Details />} />*/}
          {/*<Route path="/" element={<SearchParams />} />*/}
          {/*<Route path="/" element={<Homepage/>}/>*/}
        </Routes>
        {/*</div>*/}
      </QueryClientProvider>
    </BrowserRouter>
  );
};

export default App;
