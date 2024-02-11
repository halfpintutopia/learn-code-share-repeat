const SERVER_URL = 'http://localhost:8000';

const DEFAULT_BASE_URL = '/api';
export const ACTIVATE_USER = `${SERVER_URL}${DEFAULT_BASE_URL}/users/activate/`;
export const REGISTER_USER = `${SERVER_URL}${DEFAULT_BASE_URL}/users/register/`;
export const TOKEN_OBTAIN_API = `${SERVER_URL}${DEFAULT_BASE_URL}/auth/token/`;
export const TOKEN_REFRESH_API = `${SERVER_URL}${DEFAULT_BASE_URL}/auth/token/refresh/`;
