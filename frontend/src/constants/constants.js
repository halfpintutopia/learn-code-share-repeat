import { createUrl } from "../helpers/api";

const DEFAULT_BASE_URL = '/api';
export const ACTIVATE_USER = createUrl(`${DEFAULT_BASE_URL}/users/activate/`);
export const REGISTER_USER = createUrl(`${DEFAULT_BASE_URL}/users/register/`);
export const TOKEN_OBTAIN_API = createUrl(`${DEFAULT_BASE_URL}/auth/token/`);
export const TOKEN_REFRESH_API = createUrl(`${DEFAULT_BASE_URL}/auth/token/refresh/`);
