// apiService.ts
import axios, { AxiosRequestConfig, AxiosResponse } from "axios";

interface ApiResponse<T> {
  data: T | null;
  error: any;
}

const baseApiUrl = "http://localhost:8000/api/"; // Replace with your base URL

const executeApiRequest = async <T>(
  config: AxiosRequestConfig
): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await axios({
      ...config,
      url: baseApiUrl + config.url,
    });
    return { data: response.data, error: null };
  } catch (error: any) {
    console.error("API Error:", error);
    return { data: null, error: error.response.data.error };
  }
};

export default executeApiRequest;
