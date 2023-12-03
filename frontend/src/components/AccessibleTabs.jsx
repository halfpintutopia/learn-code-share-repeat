import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import queryString from 'query-string';

import "./sass/app.scss";

const AccessibleTabs = ({ tabs = [] }) => {
  const location = useLocation();
  const {modal} = queryString.parse(location.search);
  const [activeTab, setActiveTab] = useState(modal || tabs[0].id);
  const handleTabClick = (tabId) => {
    setActiveTab(tabId);
  };

  return (
    <div className="tabs-container">
      <ul aria-labelledby="tabs-title" className="tabs-container__list" role="tablist">
        {
          tabs.map(tab => (
            <li key={tab.id}>
              <a
                id={`tab-${tab.id}`}
                href={`#tab-${tab.id}`}
                onClick={(e) => {
                  e.preventDefault();
                  handleTabClick(tab.id);
                }}
                aria-selected={activeTab === tab.id}
                role="tab"
              >
                {tab.title}
              </a>
            </li>
          ))
        }
      </ul>

      <div className="tabs__panels flow">
        {
          tabs.map(tab => (
            <div
              key={tab.id}
              id={tab.id}
              aria-labelledby={`tab-${tab.id}`}
              hidden={activeTab !== tab.id}
            >
              {tab.content}
            </div>
          ))
        }
      </div>
    </div>
  );
};

export default AccessibleTabs;