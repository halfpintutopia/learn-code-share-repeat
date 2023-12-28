import { useEffect } from 'react';
import { useParams, useNavigate } from "react-router-dom";
import { postData } from "../helpers/fetchData";
import { ACTIVATE_USER } from "../constants/constants";

const ActivateUser = () => {
  const navigate = useNavigate();
  const { uid, token } = useParams();

  useEffect(() => {
    async function activateUser() {
      try {
        const response = await postData(ACTIVATE_USER, {
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

  }, [uid, token, navigate]);

  return null;
};

export default ActivateUser;