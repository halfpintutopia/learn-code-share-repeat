import { useEffect } from 'react';
import { useParams, useNavigate } from "react-router-dom";
import { postData } from "./fetchData";

const ActivateUser = () => {
  const navigate = useNavigate();
  const { uid, token } = useParams();

  const api = `http://localhost:8000/api/users/activate/`;

  useEffect(() => {
    async function activateUser() {
      try {
        const response = await postData(api, {
          uidb64: uid,
          token: token
        });
        if (!response.ok) {
          navigate('/join/register');
        } else {

          navigate('/join/login');
        }
      } catch (error) {
        console.error(error);
      }
    }

    // suppresses warning, doing nothing with Promise.
    activateUser().then(() => {
    });

  }, [uid, token, api, navigate]);

  return null;
};

export default ActivateUser;