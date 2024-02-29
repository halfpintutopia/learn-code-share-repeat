export const createUrl = (path) => {
  let origin = window.location.origin;
  const port = window.location.port;
  if (port === '3001') {
    // Replace the port with Django's default port (8000)
    origin = origin.replace(port, '8000');
  }
  // console.log(origin + path);
  console.log(origin + path);
  return origin + path;
};

// https://stackoverflow.com/a/41721631/8614652
export const getCookie = (name) => {
  if (!document.cookie) {
    return null;
  }

  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }
  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
};