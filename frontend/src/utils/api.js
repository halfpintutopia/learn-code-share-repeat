import { fetchWithToken } from "../helpers/fetchWithToken";

// const createEntry = (value) => {
//   return {
//     method: 'POST',
//     body: JSON.stringify(value)
//   };
// };


export const getAllVideos = async () => {
  return await fetchWithToken('/api/videos/', {
    method: 'GET',
  });
};