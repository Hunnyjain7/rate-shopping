// apiEndpoints.ts
import executeApiRequest from "./apiService";

export const clientLogin = async (data: object) => {
  const apiEndpoint = "client/login/";
  const apiConfig = {
    method: "post",
    url: apiEndpoint,
    data: data,
  };

  return executeApiRequest(apiConfig);
};

export const adminLogin = async (data: object) => {
  const apiEndpoint = "admin/login/";
  const apiConfig = {
    method: "post",
    url: apiEndpoint,
    data: data,
  };

  return executeApiRequest(apiConfig);
};
