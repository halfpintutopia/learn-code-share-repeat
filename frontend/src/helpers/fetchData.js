const fetchData = async (url = '') => {
  return await fetch(url);
};

const postData = async (url = '', data = {}) => {
  return await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
};

export { fetchData, postData };
