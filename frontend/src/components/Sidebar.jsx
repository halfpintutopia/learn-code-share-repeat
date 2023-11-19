import css from "./css/Sidebar.module.css";

const Sidebar = () => {
  return (
    <div className={css.sidebar}>
      <a href="/photos">My Photos</a>
      <a href="/illustrations">My Illustrations</a>
      <a href="/paintings">My paintings</a>
    </div>
  );
};

export default Sidebar;
