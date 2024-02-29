import { createUrl } from "../utils/helpers";

const DEFAULT_BASE_URL = '/api';
const ACTIVATE_USER = createUrl(`${ DEFAULT_BASE_URL }/users/activate/`);
const REGISTER_USER = createUrl(`${ DEFAULT_BASE_URL }/users/register/`);
const TOKEN_OBTAIN_API = createUrl(`${ DEFAULT_BASE_URL }/auth/token/`);
const TOKEN_REFRESH_API = createUrl(`${ DEFAULT_BASE_URL }/auth/token/refresh/`);
const RESET_PASSWORD = createUrl(`${ DEFAULT_BASE_URL }/accounts/password/reset/`);
const VIDEO_LIST = createUrl(`${DEFAULT_BASE_URL}/videos/`);

export {
  ACTIVATE_USER,
  REGISTER_USER,
  TOKEN_OBTAIN_API,
  TOKEN_REFRESH_API,
  RESET_PASSWORD,
  VIDEO_LIST
};