const fetchData = async (url = '') => {
  const response = await fetch(url);
  return await response.json();
};

const postData = async (url = '', data = {}) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
};

export {fetchData, postData};
