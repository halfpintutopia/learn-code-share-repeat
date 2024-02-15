import { Link } from "react-router-dom";
import Logo from "./assets/Logo";

import "./sass/main.scss";

const HeaderSimple = () => {

  return (
    <header className="secondary-header container" data-width="full">
      <section className="wrapper">
        <div className="secondary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <Logo />
          </Link>
        </div>
      </section>
    </header>
  );
};

export default HeaderSimple;