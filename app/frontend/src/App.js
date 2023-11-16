import './App.css';
import css from './App.module.css';
import Sidebar from "./components/Sidebar";
import NavBarSimple from "./components/NavBarSimple";
import RenderingList from "./components/RenderingList";
import Content from "./components/Content";

function App() {
  return (
    <div className={css.App}>
      <header className="App-header">

        {/*<img src={logo} className="App-logo" alt="logo"/>*/}
        {/*<p>*/}
        {/*	Edit <code>src/App.js</code> and save to reload.*/}
        {/*</p>*/}
        {/*<a*/}
        {/*	className="App-link"*/}
        {/*	href="https://reactjs.org"*/}
        {/*	target="_blank"*/}
        {/*	rel="noopener noreferrer"*/}
        {/*>*/}
        {/*</a>*/}
      </header>

      <NavBarSimple/>
      <Sidebar/>
      <RenderingList/>

      <Content/>

    </div>
  );
}

export default App;
