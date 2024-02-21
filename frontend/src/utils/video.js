// import { createUrl } from "../helpers/api";
import { fetchWithToken } from "../helpers/fetchWithToken";
import { TOKEN_REFRESH_API } from "../constants/constants";

// const createEntry = (value) => {
//   return {
//     method: 'POST',
//     body: JSON.stringify(value)
//   };
// };


export const getAllVideos = async () => {
  // console.log(14, localStorage.getItem('refresh_token'));
  // const response = await fetchWithToken(TOKEN_REFRESH_API, {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //     'Authorization': `Bearer ${ localStorage.getItem('access_token') }`
  //   }
  // });
  //
  // if (response.ok) {
  //   const data = await response.json();
  //   localStorage.setItem('access_token', data.access);
  //   localStorage.setItem('refresh_token', data.refresh);
  // }

  const videosResponse = await fetchWithToken('/api/videos/');

  if (videosResponse.ok) {
    return await videosResponse.json();
  } else {
    console.error(`Something went wrong with the API server: ${ videosResponse.statusText }`);
    return [];
  }
};