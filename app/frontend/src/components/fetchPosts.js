const fetchPosts = async () => {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts/");
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

export {fetchPosts, postData};
