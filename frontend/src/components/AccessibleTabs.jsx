import React from 'react';
import {Routes, Route, Link } from 'react-router-dom';

import "./sass/app.scss";

const AccessibleTabs = ({ tabs = [] }) => {

  return (
    <div className="tabs-container">
      <ul aria-labelledby="tabs-title" className="tabs-container__list" role="tablist">
        {
          tabs.map(tab => (
            <li key={tab.id}>
              <Link
                to={`/${tab.id}`}
                role="tab"
              >
                {tab.title}
              </Link>
            </li>
          ))
        }
      </ul>

      <Routes>
        {
          tabs.map(tab => (
            <Route
              key={tab.id}
              path={`/${tab.id}`}
              element={
                <div className="tabs__panels flow">
                  {tab.content}
                </div>
              }
            />
          ))
        }
      </Routes>
    </div>
  );
};

export default AccessibleTabs;