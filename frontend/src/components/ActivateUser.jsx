import { useEffect } from 'react';
import { useParams, useNavigate } from "react-router-dom";

const ActivateUser = () => {
  const navigate = useNavigate();
  const { uid, token } = useParams();

  const api = `/api/users/activate/${uid}/${token}/`;

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(api);
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
    fetchData().then(() => {
    });

  }, [uid, token, api, navigate]);

  return null;
};

export default ActivateUser;