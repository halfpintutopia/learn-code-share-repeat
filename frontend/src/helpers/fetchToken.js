import { TOKEN_REFRESH_API } from "../constants/constants";

const fetchToken = async function fetchWithTokenRefresh(url, options) {
  const res = await fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': `Bearer ${localStorage.getItem(('access_token'))}`
    }
  });

  if (res.status === 401) {
    const refreshRes = await fetch(TOKEN_REFRESH_API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        refresh: localStorage.getItem('refresh_token')
      })
    });

    if (refreshRes.ok) {
      const data = await refreshRes.json();
      localStorage.setItem('access_token', data.access);

      const retryRes = await fetch(url, {
        ...options,
        headers: {
          ...options.headers,
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
      });

      if (retryRes.ok) {
        return retryRes;
      }
    } else {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');

      // Redirect to login page
      // history.push('/join/login');
    }
  }
  return res;
};

export { fetchToken };