import { fetchWithToken } from "./fetchWithToken";
import { RESET_PASSWORD, VIDEO_LIST } from "../constants/constants";
import { getCookie } from "./helpers";

// const createEntry = (value) => {
//   return {
//     method: 'POST',
//     body: JSON.stringify(value)
//   };
// };


export const getAllVideos = async () => {
  return await fetchWithToken(VIDEO_LIST, {
    method: 'GET',
  });
};

export const resetPassword = async (email) => {
  // const csrfToken =
  const response = await fetch(RESET_PASSWORD, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ email }),
  });

  if (response.ok) {
    return response.json();
    // Handle successful password reset request
  } else {
    // Handle error
  }
};