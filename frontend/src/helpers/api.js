export const createUrl = (path) => {
  let origin = window.location.origin;
  const port = window.location.port;
  if (port === '3001') {
    // Replace the port with Django's default port (8000)
    origin = origin.replace(port, '8000');
  }
  console.log(origin + path);

  return origin + path;
};