import { TOKEN_OBTAIN_API, TOKEN_REFRESH_API } from "../constants/constants";

const fetchToken = async (url, options) => {
  const obtainTokenRes = await fetch(TOKEN_OBTAIN_API, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: options?.body ? options.body : null
  });

  if (obtainTokenRes.ok) {
    const data = await obtainTokenRes.json();
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
  }

  return obtainTokenRes;
};

const fetchWithToken = async (url, options = {}) => {
  const accessToken = localStorage.getItem('access_token');
  if (accessToken !== '') {
    let res = await fetch(url, {
      method: options?.method || 'GET',
      body: options?.body ? options.body : null,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${ accessToken }`,
        ...options.headers
      }
    });

    if (!res.ok && res.status === 401) { // 401 Unauthorized means token is expired
      const refreshToken = localStorage.getItem('refresh_token');
      let refreshRes;
      if (refreshToken) {
        refreshRes = await fetch(TOKEN_REFRESH_API, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            refresh: refreshToken
          })
        });
      }

      if (refreshRes.ok) {
        const data = await refreshRes.json();
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);

        res = await fetch(url, {
          method: options?.method || 'GET',
          body: options?.body ? JSON.stringify(options.body) : null,
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${ localStorage.getItem('access_token') }`,
            ...options.headers
          }
        });
      } else {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
      }
    }
    return res;
  }
};

export { fetchToken, fetchWithToken };