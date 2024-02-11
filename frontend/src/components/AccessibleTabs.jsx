import React from 'react';
import { Link } from 'react-router-dom';

import "./sass/main.scss";

const AccessibleTabs = ({ tabs = [], type }) => {
  const selectedTab = tabs.find(tab => tab.id === type);

  return (
    <div className="tabs-container">
      <ul aria-labelledby="tabs-title" className="tabs-container__list" role="tablist">
        {
          tabs.map(tab => (
            <li key={ tab.id }>
              <Link
                to={ `/join/${ tab.id }` }
                role="tab"
                aria-selected={ type === `${ tab.id }` }
              >
                { tab.title }
              </Link>
            </li>
          ))
        }
      </ul>

      {
        selectedTab && (
          <div className="tabs__panels flow">
            { selectedTab.content }
          </div>
        )
      }
    </div>
  );
};

export default AccessibleTabs;